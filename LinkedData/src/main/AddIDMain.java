package main;

import model.JSON_API;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.Charset;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Created by Jan-Peter Schmidt on 15.07.2017.
 *
 * Adapted from: https://stackoverflow.com/questions/23724221/java-append-object-to-json
 *
 */
public class AddIDMain {

    public static void main(String[] args) {
        String progwebFile = "1_data/2_preprocessed/progweb_preprocessed.json";
        String linkedDataFile = "LinkedData/data/linked_data_no_id.json";

        try {
            String progwebString = CrawlerMain.readFile(progwebFile, Charset.forName("UTF-8"));
            String linkedDataString = CrawlerMain.readFile(linkedDataFile, Charset.forName("UTF-8"));

            JSONArray array = new JSONArray(progwebString);
            JSONArray linkedData = new JSONArray(linkedDataString);

            Integer maxId = -1;

            for(int i=0; i<array.length();i++) {

                JSONObject object = array.getJSONObject(i);

                if(object.has("id") && object.has("api_name")) {
                    Integer id = (Integer) object.get("id");
                    String name = (String) object.get("api_name");

                    maxId= (maxId < id) ? (id) : (maxId);

                    for(int j=0; j<linkedData.length(); j++) {

                        JSONObject ldObject = linkedData.getJSONObject(j);
                        if(ldObject.has("api_name") && name.equals(ldObject.get("api_name").toString().replace(" API",""))) {

                            ldObject.put("id",id);
                            System.out.println(ldObject.get("api_name") + " --> " +id);
                            break;

                        }

                    }

                }

            }

            //Pruefe auf fehlende IDs
            int counter = 0;
            int counter2 = 0;

            for(int i=0; i<linkedData.length(); i++) {

                JSONObject object = linkedData.getJSONObject(i);
                if(!object.has("id")) {
                    counter++;
                    //Fuege eine nicht bereits vergebene neue ID ein
                    object.put("id",maxId++);
                }

            }

            for(int i=0; i<linkedData.length(); i++) {

                JSONObject object = linkedData.getJSONObject(i);
                if(!object.has("id")) {
                    counter2++;
                }

            }

            PrintWriter writer = new PrintWriter("data/linked_data.json", "UTF-8");

            writer.print(linkedData.toString().replace("},","},\n"));
            writer.close();

            System.out.println("Ready! " +counter + " APIs without ID! Reduced to " + counter2 + " by creating IDs");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}