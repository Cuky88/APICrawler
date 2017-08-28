package main;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Iterator;

import model.API;
import model.RFDEntry;

public class CrawlerMain {
	
	public static ArrayList<RFDEntry> entries = new ArrayList<RFDEntry>();
	public static ArrayList<String> predicateList = new ArrayList<String>();

	public static void main(String[] args) {


		storeTxtToList();

		Path map = Paths.get("KDD Seminar");
		System.out.println(map.toAbsolutePath().toString());

		System.out.println("***** STORED TO LIST ******");
		
		//analyzeDuplicates();
		
		//getAPITitles();

		Iterator<RFDEntry> iterator = entries.iterator();

		while(iterator.hasNext()) {

			RFDEntry entry = iterator.next();

			API api = API.getOrCreate(entry.getSubject());
			api.setProperty(entry);

		}

		System.out.println(API.getList().size() + " APIs found");

		API.createCSV();

		System.out.println(" ***** FINISHED ********");


	}

	public static String readFile(String path, Charset encoding)
			  throws IOException 
	{
	  byte[] encoded = Files.readAllBytes(Paths.get(path));
	  return new String(encoded, encoding);
	}
	
	public static void storeTxtToList() {
		
		String fileName = "KDD Seminar/lwapis_v1.txt";
		
		try {
			String content = readFile(fileName, Charset.forName("UTF-8"));
			String[] lines = content.split("\\r\\n|\\n|\\r");
			
			System.out.println("Found " + lines.length + " lines.");

			int counter = 0;
			
			for(String line:lines) {
				
				int arrayCounter = 0;
				int beginIndex = 0;				
				
				String[] parts = new String[4];
				
				if(line.contains("\"")) {
					
					//split complex triples
					boolean splitabble = true;
					for(int i=0; i<line.length();i++) {
						
						if(line.charAt(i)=='"' && line.charAt(i-1)!='\\') {
							
							//Toogle SplitNot
							splitabble = !splitabble;
							
						}
						
						if(line.charAt(i)==' ' && splitabble) {
							
							parts[arrayCounter++] = line.substring(beginIndex, i);
							beginIndex = i+1;
						}
						
					}

				} else {
					parts = line.split(" ");
				}
				
				entries.add(new RFDEntry(parts[0],parts[1],parts[2]));
				
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
		
	}
	
	//Prints all predicates without duplicates
	public static void createPredicateList() {
		
		Iterator<RFDEntry> iterator = entries.iterator();

		int counter = 0;
		
		while(iterator.hasNext()) {

			RFDEntry entry = iterator.next();
			
			//System.out.println("Check " + entry.getPredicate());
			
			if(!predicateList.contains(entry.getPredicate())) {
				
				predicateList.add(entry.getPredicate());
				
			}
			
		}
		
		//Predicate ausgeben
		/*Iterator<String> iteratorPredicate = predicateList.iterator();
		
		while(iteratorPredicate.hasNext()) {
			
			System.out.println(iteratorPredicate.next());
			
		}*/
		
		
	}
	
	public static ArrayList<String> getAPITitles() {
		
		ArrayList<String> titles = new ArrayList<String>();
		
		Iterator<RFDEntry> iterator = entries.iterator();
		while(iterator.hasNext()) {
			
			RFDEntry entry = iterator.next();
			
			//<http://purl.org/dc/terms/title>
			
			if(entry.getPredicate().equals("<http://xmlns.com/foaf/0.1/homepage>")) {
				titles.add(entry.getSubject());
			}
			
			
		}
		
		System.out.println("Found " + titles.size() + " homepages.");
		
		return titles;
		
		
	}
	
	public static String convertForURL(String string) {
		
		return string.replace(" ","-").replace("\"","").toLowerCase();
		
	}

	public static ArrayList<RFDEntry> getEntries() {
		return entries;
	}

	public static ArrayList<String> getPredicateList() {
		return predicateList;
	}
}