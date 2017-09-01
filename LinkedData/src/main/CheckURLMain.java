package main;

import model.JSON_API;
import org.json.JSONArray;
import org.json.JSONObject;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.*;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

/**
 * Created by Jan-Peter on 04.06.2017.
 */
public class CheckURLMain {

    public static void main(String[] args) {

        ArrayList<Integer> length = new ArrayList<>();

        //Stores all APIs
        ArrayList<JSON_API> list = new ArrayList<JSON_API>();

        //Stores all APIs where a body can be loaded from the website
        ArrayList<JSON_API> bodyList = new ArrayList<JSON_API>();

        int counterBlog = 0;

        //Try to read the linked_data_sparql.json - dump from SPARQL Endpoint of the LinkedData with relevant information about the api
        try {
            String fileContent = CrawlerMain.readFile("LinkedData/data/linked_data_sparql.json", Charset.forName("UTF-8"));

            JSONObject file = new JSONObject(fileContent);
            JSONObject results = file.getJSONObject("results");
            JSONArray apis = results.getJSONArray("bindings");

            for(int i=0; i<apis.length(); i++) {

                JSONObject current = apis.getJSONObject(i);

                JSON_API api = new JSON_API();
                list.add(api);

                api.setName(current.getJSONObject("name").getString("value"));
                api.setHomepage(current.getJSONObject("homepage").getString("value"));
                if(!current.isNull("blog") && current.getJSONObject("blog").getString("value")!=null) {
                    api.setBlog(current.getJSONObject("blog").getString("value"));
                    counterBlog++;
                    //System.out.println(api.getBlog() + "<-- set");
                }

                if(!current.isNull("api")) {
                    api.setURI(current.getJSONObject("api").getString("value"));
                }

            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        //How many APIs do we have at all?
        System.out.println(list.size() + " APIs.");

        //How many APIs do provide an URL?
        System.out.println(counterBlog + " Links für APIs gefunden.");

        //Go through the whole API list and try to connect to the website / programmable web
        Iterator<JSON_API> iterator = list.iterator();

        int counter = 0;

        while(iterator.hasNext()) {

            JSON_API api = iterator.next();

            //Run crawler for each API in his own Thread to speed up the process (Waiting for server response takes some seconds for each API)
            new Thread() {

                public void run() {

                    //Deprecated - is now in Selcuks Crawler implemented
                    /*
                    Check Homepage -> ProgrammableWeb
                    try {
                        //System.out.println("Check URL: \"" + api.getHomepage() + "\"");
                        String title = Jsoup.connect(api.getHomepage()).get().getElementsByTag("title").get(0).data();
                    } catch (Exception e) {
                        //e.printStackTrace();
                        api.setHomepage("");
                        System.out.println("No hp for " + api.getName());
                    }*/

                    int counterABC = 0;

                    //Try to connect to the given URL
                    try {

                        //No API Link given in Linked Data Set
                        if(api.getBlog()==null) {

                            api.setError("No link");

                        } else {
                            counterABC++;

                            //Connect
                            Document page = Jsoup.connect(api.getBlog()).get();

                            //Fetch data from html body - only take letters or numbers
                            String body =Jsoup.parse(page.html()).text().replaceAll("[^A-Za-z0-9 ]","");
                            System.out.println(body.length() + " chars found");
                            length.add(body.length());
                            api.setBody(body);

                            //Add API to list that only includes APIs with accessable websites
                            bodyList.add(api);

                            //Try also to store the keywords from the webpage given in meta-data
                            try {
                                String keywords = page.select("meta[name=keywords]").get(0).attr("content").replaceAll("[^A-Za-z0-9 ]", "");
                                api.setKeywords(keywords);
                            } catch(Exception eKeywords) {

                            }

                            JSON_API.counter++;
                        }

                    }
                    //If accessing the given blog link is not possible - try to repair the link
                    catch (Exception e) {
                        //e.printStackTrace();
                        //System.out.println(e.getClass().getCanonicalName() + " for \"" +  api.getBlog() + "\"" + ", for API: " +api.getName());

                        //Set deprecated, because given Blog URL does not work
                        api.setDeprecated(true);

                        //HTTP Status Error or Unknown Host Exception are possible to repair
                        if(e.getClass().getCanonicalName().equals("org.jsoup.HttpStatusException") ||
                                e.getClass().getCanonicalName().equals("java.net.UnknownHostException")) {

                            //Check for Subdomain - avoid subdomain -> use Toplevel domain
                            int numDots = org.apache.commons.lang.StringUtils.countMatches(api.getBlog(),".");
                            int numSlashes = org.apache.commons.lang.StringUtils.countMatches(api.getBlog(),"/");

                            String newURL = "";
                            //Subdomain detected -> get Toplevel-Domain
                            if(numDots>1 && !api.getBlog().matches("(.*).html(.*)|(.*).php(.*)|(.*).shtml(.*)")) {

                                int startSubdomain = api.getBlog().indexOf("//");
                                int endSubdomain = api.getBlog().indexOf(".");
                                newURL = api.getBlog().substring(0,startSubdomain+2) + api.getBlog().substring(endSubdomain+1,api.getBlog().length());

                                //Check if real subdomain was detected or only 'www.' - if it is www cut again.
                                if(api.getBlog().substring(startSubdomain+2,endSubdomain).equals("www") && org.apache.commons.lang.StringUtils.countMatches(newURL,".")>1) {
                                    //System.out.println("Catched www " + newURL);

                                    startSubdomain = newURL.indexOf("//");
                                    endSubdomain = newURL.indexOf(".");
                                    newURL = newURL.substring(0, startSubdomain + 2) + newURL.substring(endSubdomain + 1, newURL.length() - 1);
                                }

                                //System.out.println("Subdomain editing: " + api.getBlog() + " -> " + newURL);

                                //Store improved URL
                                api.setImproved(true);

                            }
                            //Path detected -> delete Path
                            if(numSlashes > 2) {
                                //Cut path and check URL again
                                int slashCounter = 0;
                                int position = -1;

                                //Use toplevel domain without subdomain if already created
                                String url = (newURL.equals("") ? (api.getBlog()) : (newURL));

                                for(int i=0; i<url.length(); i++) {

                                    if(url.charAt(i)=='/') {
                                        slashCounter++;
                                        position = i;
                                    }

                                    if(slashCounter>=3) {

                                        break;

                                    }

                                }

                                newURL = url.substring(0, position);

                                //System.out.println("Path editing: " + url + " -> " + newURL);

                                api.setImproved(true);
                            }

                            api.setImprovedURL(newURL);


                            //Try to connect to new generated URL
                            try {

                                //If no improvement could be achieved throw old error again
                                if(newURL==null || newURL.equals("")) {
                                    throw e;
                                }

                                //Connect again with new URL
                                Document page = Jsoup.connect(newURL).get();

                                //Fetch data from body again - only use letters and numbers
                                String body =Jsoup.parse(page.html()).text().replaceAll("[^A-Za-z0-9 ]","");
                                System.out.println(body.length() + " chars found -- new created URL");
                                api.setBody(body);
                                length.add(body.length());

                                JSON_API.counterImproved++;

                                bodyList.add(api);

                                //Try to fetch keywords
                                try {
                                    String keywords = page.select("meta[name=keywords]").get(0).attr("content").replaceAll("[^A-Za-z0-9 ]", "");
                                    api.setKeywords(keywords);
                                } catch(Exception eKeyword) {

                                }

                                JSON_API.counter++;

                                //Set flag that shows whether improvement was successful
                                api.setImproveSuccess(true);

                            } catch(Exception e1){

                                //Log error if improvement failed also
                                api.setError(e1.getClass().getCanonicalName());

                                //System.out.println("Improved Version..." + e.getClass().getCanonicalName() + " for \"" +  api.getImprovedURL() + "\"" + ", for API: " +api.getName());

                                //e1.printStackTrace();

                            }

                        } else {
                            //in all other exceptions cases the improvement won't work -> log error directly
                            api.setError(e.getClass().getCanonicalName());
                        }
                    }

                    //System.out.println(counterABC);

                    /**
                     * --- Deprecated ---
                     * Access to PW is handled by Selcuk in his crawler
                     *
                     */
                    /* if Homepage is set and Blog is empty -> try to get link from ProgrammableWeb
                    if(api.getBlog()==null || api.getBlog().equals("") && api.getHomepage()!=null && !api.getHomepage().equals("")) {

                        //Take Blog from Programmable web
                        try {
                            Document document = Jsoup.connect(api.getHomepage()).get();
                            Elements labels = document.getElementsContainingText("API Portal / Home Page");
                            System.out.println(labels.get(0).nextElementSibling().data() + " <- URL?");

                        } catch (IOException e) {
                            e.printStackTrace();
                        }


                    }*/

                    //System.out.println(api);

                }

            }.start();

        }

        /**
         * Due to the waiting time for the server several threads are running in parallel. To simplify
         * the detection if all threads have done their work properly the program is waiting for some user input,
         * so that human can decide whether all relevant data have been grapped from the web.
         *
         * One can just wait until no more findings are logged in the console and start with number 1-3 the wished
         * output type.
         *
         * 1 - Prints all found bodies and keywords into a JSON-File
         * 2 - Prints statistic data into a CSV-File which are relevant for the research on quality of the linked data set
         * 3 - Prints all found bodies and keywords into a JSON-File which has the same format as Selcuks file
         *
         */

        //Check
        //Do something if enter is pressed

        Scanner scanner = new Scanner(System.in);
        String readString = scanner.nextLine();
        System.out.println(readString);

        //Create JSON
        if (readString.equals("1")) {

            System.out.println("Start creating JSON... " + bodyList.size());

            //Write all BodyAPIs to JSON
            try {
                PrintWriter writer = new PrintWriter("data_final/data_complete.json", "UTF-8");
                createJSONHead(writer);

                Iterator<JSON_API> iterator1 = bodyList.iterator();

                int counter1 = 0;

                while(iterator1.hasNext()) {

                    JSON_API api = iterator1.next();

                    writer.println("{ \"name\": { \"type\": \"literal\", \"value\": \"" + api.getName() +"\" }\t, \"api\": { \"type\": \"uri\", \"value\": \"" + api.getURI() + "\" }\t, \"homepage\": { \"type\": \"uri\", \"value\": \"" + api.getHomepage() + "\" }\t, \"blog\": { \"type\": \"uri\", \"value\": \"" + api.getBlog() + "\" }\t, \"endpoint\": { \"type\": \"literal\", \"value\": \"" + api.getEndpoint() + "\" }, \"keywords\": { \"type\": \"literal\", \"value\": \"" + api.getKeywords() + "\" }, \"blogDescr\": { \"type\": \"literal\", \"value\": \"" + api.getBody() + "\" }},");
                    counter1++;

                }

                System.out.println("Ready! " + counter1);

                //Close JSON
                closeJSON(writer);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }

        }
        //Create CSV for URL evaluation
        else if(readString.equals("2")) {

            System.out.println("Found " + JSON_API.counterImproved + " APIs with new URLs");

            System.out.println("Create Evaluation.csv...");

            try{
                PrintWriter writer = new PrintWriter("urlEvaluation.csv", "UTF-8");

                Iterator<JSON_API> iterator1 = list.iterator();

                writer.println("Name; Blog; Error; Improved; new URL; accessable");

                int counter1 = 0;

                while(iterator1.hasNext()) {

                    JSON_API api = iterator1.next();

                    writer.println(api.getName() + ";" +  api.getBlog() + ";" +  api.getError()+ ";" + api.isImproved() + ";" + api.getImprovedURL() + ";" + api.isImproveSuccess());
                    counter1++;

                }

                System.out.println("Ready! " + counter1);


            } catch (IOException e) {
                // do something
            }

        }

        //Create JSON in Selcuks Format
        else if(readString.equals("3")) {

            System.out.println("Create JSON...");

            try{
                PrintWriter writer = new PrintWriter("LinkedData/data/data_json_formatted.json", "UTF-8");

                writer.println("[");
                Iterator<JSON_API> iterator1 = bodyList.iterator();

                while(iterator1.hasNext()) {

                    JSON_API api = iterator1.next();
                    writer.println(api.getSelcukJSON());

                }

                writer.println("]");
                writer.close();

                System.out.println("Ready!");

            } catch (IOException e) {
                // do something
                e.printStackTrace();
            }

        }
        //Set depreacted Tags to RDF File
        else if(readString.equals("4")) {

            String triples = "";

            Iterator<JSON_API> iterator1 = list.iterator();
            int counterTriples = 0;

            //Create deprecated triples for all APIs where an error occured while fetching Blog URL
            while(iterator1.hasNext()) {

                JSON_API api = iterator1.next();

                if(api.isDeprecated()) {

                    triples = triples + "\n<" + api.getURI() + "> <http://www.w3.org/2002/07/owl#deprecated> \"true\"^^<http://www.w3.org/2001/XMLSchema#boolean>.";
                    counterTriples++;

                }

            }

            //Write triples to File
            try {
                PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("LinkedData/lwapis_v1.txt", true)));
                out.println(triples);
                out.close();
            } catch (IOException e) {
                //exception handling left as an exercise for the reader
            }

            System.out.println(counterTriples + " triples added!");

            //Some statistical output
        } else if(readString.equals("5")) {

            Iterator<Integer> iteratorLength = length.iterator();
            Integer sum = 0;

            while(iteratorLength.hasNext()) {

                sum = sum + iteratorLength.next();

            }

            System.out.println(sum + ", " + length.size());

            double average = sum / length.size();
            double variance = variance(length, average);


            System.out.println("Mean of body length: " + average + ", variance=" + variance);

        }
        if (scanner.hasNextLine())
            readString = scanner.nextLine();
        else
            readString = null;

    }



    private static void createJSONHead(PrintWriter writer) {

        writer.println("{ \"head\": { \"link\": [], \"vars\": [\"name\", \"api\", \"homepage\", \"blog\", \"endpoint\"] },");
        writer.println("  \"results\": { \"distinct\": false, \"ordered\": true, \"bindings\": [");

    }

    private static void closeJSON(PrintWriter writer) {

        writer.println("] } }");
        writer.close();

    }

    //Taken from https://stackoverflow.com/questions/26532832/calculating-sample-variance-in-java-but-is-giving-the-wrong-answer-when-inserti?answertab=oldest#tab-top

    public static double variance(ArrayList<Integer> list, double avg) {
        double sumDiffsSquared = 0.0;
        for (int value : list)
        {
            double diff = value - avg;
            diff *= diff;
            sumDiffsSquared += diff;
        }
        return sumDiffsSquared  / (list.size()-1);
    }

}