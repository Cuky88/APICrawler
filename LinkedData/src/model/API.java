package model;

import main.CrawlerMain;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * Created by Jan-Peter on 19.05.2017.
 */
public class API {

    private static HashMap<String, API> list = new HashMap<String, API>();
    private HashMap<String,String> properties;

    public API() {
        this.properties = new HashMap<String,String>();
    }


    public static API getOrCreate(String name) {

        if(list.containsKey(name)) {

            return list.get(name);

        } else {

            API api = new API();

            list.put(name, api);

            return new API();

        }


    }

    public void setProperty(RFDEntry entry) {

        if(properties.containsKey(entry.getPredicate())) {

            String value = properties.get(entry.getPredicate()) + ", " + entry.getObject();

            properties.remove(entry.getPredicate());
            properties.put(entry.getPredicate(), value);

        } else {

            properties.put(entry.getPredicate(), entry.getObject());

        }

        //System.out.println(entry.getSubject() + ": Set " + entry.getPredicate() + " with value \"" + entry.getObject() + "\"");

    }

    public static HashMap<String, API> getList() {
        return list;
    }

    public HashMap<String, String> getProperties() {
        return properties;
    }

    public static void createCSV() {

        try {
            PrintWriter out = new PrintWriter("KDD Seminar/out/database.csv");

            Iterator<Map.Entry<String, API>> apiIterator = list.entrySet().iterator();

            out.println(constructHead());

            while (apiIterator.hasNext()) {

                Map.Entry<String, API> entry = apiIterator.next();

                out.println(entry.getValue().getCSVLine(entry.getKey()));

            }

        } catch(IOException ioe) {
            ioe.printStackTrace();
        }

    }

    private static String constructHead() {

        String head = "Name;";

        CrawlerMain.createPredicateList();

        Iterator<String> iterator = CrawlerMain.getPredicateList().iterator();

        while(iterator.hasNext()) {

            head = head + iterator.next() + ";";

        }

        return head;

    }

    private String getCSVLine(String name) {

        String csv=name+";";

        Iterator<String> predicateIterator = CrawlerMain.getPredicateList().iterator();

        while(predicateIterator.hasNext()) {

            String predicate = predicateIterator.next();
            Iterator<Map.Entry<String,String>> propertyIterator = properties.entrySet().iterator();

            while(propertyIterator.hasNext()) {

                Map.Entry<String,String> property = propertyIterator.next();
                if(property.getKey().equals(predicate)) {

                    csv = csv + property.getValue();

                }

            }

            csv = csv + ";";

        }

        return csv;

    }
}
