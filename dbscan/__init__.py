import readwrite
import clustering


path = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/1_data/2_preprocessed/progweb_preprocessed.json'

save_path = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/dbscan/dest/db_jaccard.json'


json = readwrite.read(path)

input = json[:3000]

labels = clustering.main(input, 0.8, 2)

print labels

readwrite.write(save_path,labels)