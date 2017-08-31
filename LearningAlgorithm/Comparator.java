package main;

import jdk.nashorn.internal.parser.JSONParser;
import org.json.JSONArray;
import org.json.JSONObject;
import org.jsoup.parser.Parser;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.*;

/**
 * Created by Jan-Peter Schmidt on 17.07.2017.
 */
public class Comparator {

    public static void main(String[] args) {

        //String manualPath = "data/manual_real.json";
        //String machinePath = "data/kmeans.json";
        String manualPath = "data/manual_test.json";
        String machinePath = "data/machine_cluster.json";
        String[] parameter = {"dist","k","dim"};
        String qualityPath = "data/pyComp.json";

        ArrayList<Integer> tp = new ArrayList<>();
        ArrayList<Integer> fp = new ArrayList<>();
        ArrayList<Integer> fn = new ArrayList<>();
        ArrayList<Integer> tn = new ArrayList<>();

        ArrayList<Double> recallList = new ArrayList<>();
        ArrayList<Double> precisionList = new ArrayList<>();

        if(args.length>1) {

            machinePath = args[0];
            manualPath = args[1];
            parameter = args[0].split("_");
            if(parameter.length>3) {
                parameter[0] = parameter[0] + "_" + parameter[1];
                parameter[0] = parameter[0].replace("results/kmeansresults/", "");
                parameter[1] = parameter[2];
                parameter[2]= parameter[3].replace(".json","");
            } else {
                parameter[2] = parameter[2].replace(".json", "");
                parameter[0] = parameter[0].replace("results/kmeansresults/", "");
            }
            System.out.println("Start with manualPath " + manualPath + ", " + machinePath + ", dist=" + parameter[0] +
                    ", k=" + parameter[1] + ", dim=" + parameter[2]);
        }

        try {
            JSONArray machineJSON = new JSONArray(CrawlerMain.readFile(machinePath, Charset.forName("UTF-8")));
            JSONArray manualJSON = new JSONArray(CrawlerMain.readFile(manualPath, Charset.forName("UTF-8")));
            JSONArray machineJSONreduced = new JSONArray();

            //Minimize machineJSON to manualSize (others are not needed)
            System.out.println("Size API list original : " + machineJSON.length());
            ArrayList<Integer> deletions = new ArrayList<>();

            int length = machineJSON.length();

            for(int a=0; a<length;a++) {
                for(int b=0; b<manualJSON.length();b++) {
                    if(machineJSON.getJSONObject(a).getInt("id")==manualJSON.getJSONObject(b).getInt("id")) {
                        machineJSONreduced.put(machineJSON.getJSONObject(a));
                        break;
                    }
                }
            }

            System.out.println("Size API list reduced : " + machineJSONreduced.length());

            //Old one is not needed anymore
            machineJSON = machineJSONreduced;

            ArrayList<Integer> examinedCluster = new ArrayList<Integer>();

            System.out.println(" ------- Start comparing -------");

            //Iteratoe over all manual clustered APIs
            for(int i=0; i<manualJSON.length(); i++) {

                //System.out.println("Check cluster of " + manualJSON.getJSONObject(i).get("name"));

                JSONObject api = manualJSON.getJSONObject(i);
                Integer cluster = (api.has("cluster_id") ? (api.getInt("cluster_id")) : (-1));

                if(cluster != -1 && !examinedCluster.contains(cluster)) {

                    //System.out.println(cluster + " is cluster id.");

                    //Find apis that are contained in this cluster
                    ArrayList<Integer> containedAPIs = new ArrayList<>();

                    for (int j = 0; j < manualJSON.length(); j++) {

                        JSONObject obj = manualJSON.getJSONObject(j);

                        if(obj.has("cluster_id") && obj.get("cluster_id")==cluster) {
                            containedAPIs.add(obj.getInt("id"));
                        }

                    }

                    //Check which Cluster is most identical to manual clustered one
                    HashMap<Integer, Integer> clusterCounter = new HashMap<>();

                    for(int k=0; k < machineJSON.length(); k++) {

                        JSONObject obj = machineJSON.getJSONObject(k);
                        if(containedAPIs.contains((Integer) obj.get("id"))) {

                            Integer clusterIDOfAPI = (obj.has("cluster_id") ? obj.getInt("cluster_id") : -1);
                            Integer value = -1;

                            if(clusterIDOfAPI!=-1 && (value = clusterCounter.get(clusterIDOfAPI))!=null) {
                                clusterCounter.put(clusterIDOfAPI,clusterCounter.get(clusterIDOfAPI)+1);
                            } else if(clusterIDOfAPI!=-1) {
                                clusterCounter.put(clusterIDOfAPI,1);
                            }

                        }

                    }

                    //System.out.println(clusterCounter.size() + "size");

                    //System.out.println("1:"+clusterCounter.get(1) + " 2:" + clusterCounter.get(22));

                    Integer keyMax = -1;
                    Integer maxValue = -1;

                    Set<Map.Entry<Integer, Integer>> set = clusterCounter.entrySet();
                    Iterator<Map.Entry<Integer,Integer>> iterator = set.iterator();

                    while(iterator.hasNext()) {

                        Map.Entry<Integer, Integer> entry = iterator.next();
                        if(entry.getValue() > maxValue) {
                            maxValue = entry.getValue();
                            keyMax = entry.getKey();
                        }
                    }

                    //Cluster ID mit größter Übereinstimmung
                    if(keyMax!=-1) {

                        //System.out.println(keyMax);

                        //Get machine APIs that are in this cluster
                        ArrayList<Integer> containedMachineAPIs = new ArrayList<>();

                        for (int j = 0; j < machineJSON.length(); j++) {

                            JSONObject obj = machineJSON.getJSONObject(j);

                            if (obj.has("cluster_id") && obj.get("cluster_id") == keyMax) {
                                //System.out.println("add " + obj.get("name"));
                                containedMachineAPIs.add(obj.getInt("id"));
                            }
                        }

                        //Calculate Precision and Recall
                        for (int l = 0; l < machineJSON.length(); l++) {

                            JSONObject obj = machineJSON.getJSONObject(l);

                            Integer apiID = obj.getInt("id");

                            if (!containedMachineAPIs.contains(apiID) && !containedAPIs.contains(apiID)) {
                                tn.add(apiID);
                            } else if (containedAPIs.contains(apiID) && containedMachineAPIs.contains(apiID)) {
                                tp.add(apiID);
                            } else if (containedMachineAPIs.contains(apiID) && !containedAPIs.contains(apiID)) {
                                fp.add(apiID);
                            } else if (!containedMachineAPIs.contains(apiID) && containedAPIs.contains(apiID)) {
                                fn.add(apiID);
                            }
                        }

                    }
                }

                if(!examinedCluster.contains(cluster)) {
                    examinedCluster.add(cluster);
                    System.out.println("Done this for " + examinedCluster.size() + " Clusters.");
                    System.out.println("tp:" + tp.size() + ", fp: " + fp.size() + ", fn: " + fn.size() + ", tn: " + tn.size());

                    double precision = (double) tp.size() / (tp.size() + fp.size());
                    double recall = (double) tp.size() / (tp.size() + fn.size());

                    System.out.println("Precision: " + precision);
                    System.out.println("Recall: " + recall );

                    if(!Double.isNaN(precision) && !Double.isNaN(recall)) {
                        precisionList.add(precision);
                        recallList.add(recall);
                    }

                    System.out.println("-----------------------");

                    tp.clear();
                    tn.clear();
                    fp.clear();
                    fn.clear();

                }

            }

            double precisionSum = 0;
            Iterator<Double> iterator = precisionList.iterator();
            while(iterator.hasNext()) {

                Double incr = iterator.next();
                //System.out.println(incr);
                precisionSum = precisionSum + incr;

            }

            double recallSum = 0;
            Iterator<Double> iterator1 = recallList.iterator();
            while(iterator1.hasNext()) {

                Double incr = iterator1.next();
                //System.out.println(incr);
                recallSum = recallSum + incr;

            }

            double precisionAvg = precisionSum / precisionList.size();
            double recallAvg = recallSum / recallList.size();

            System.out.println("Precision: " + precisionAvg);
            System.out.println("Recall: " + recallAvg);

            writeResult(precisionAvg, recallAvg, parameter);



        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void writeResult(double precision, double recall, String[] parameter) {

        String path = "finalResults.csv";
        File file = new File(path);

        try {
            if (!file.isFile()) {

                file.createNewFile();
                String line = "Precision;Recall;Distance;k;Dimension\n";
                Files.write(Paths.get(path), line.getBytes(), StandardOpenOption.APPEND);

            }

            // dist_k_dim

            String line = precision + ";" + recall + ";" + parameter[0] + ";" + parameter[1] + ";" + parameter[2] + ";\n";
            Files.write(Paths.get(path), line.getBytes(), StandardOpenOption.APPEND);

        } catch(IOException ioe) {
            ioe.printStackTrace();
        }
    }

}
