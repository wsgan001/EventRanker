import random
import pickle
# annotation for world cup
def unpickle(filename):
    f = open(filename,"rb") 
    heroes = pickle.load(f)
    return heroes

#soccer_annotated_clusters = {0: [6,20,21,22,25,30,31,36,37,38,39,42,43,46,48,49,50], 1: [27,40,41], 2: [17,18,24,32], 3: [0,5,9,10,13,19], 4: [1,2,7,8,11,12,15,47], 5: [4,35], 6: [14], 7: [16], 8: [23,26,34], 9: [28,44], 10: [29,33,45]}
#arabspring_annotated_clusters = {0: [0,6,35,49], 1: [31,30,46,9,37,44], 2: [10,12,13,17,34,42], 3: [39,40,48,25,29], 4: [23,19,20], 5: [51,21,26,38,45]}
#hongkong_annotated_clusters = {0:[1, 2, 8, 10, 17, 20, 26, 27], 1:[0, 18, 21, 23, 29, 30, 33, 42],2:[19, 29, 31, 40, 49],3:[9, 12, 15],4:[6, 13, 16, 22, 38, 41],5:[ 25, 45, 47, 48],6:[5, 9, 11, 28],7:[14, 39],8:[24, 32, 34, 46, 50],9:[35, 36, 37]}
stockmarket_annotated_clusters = {0:[22,7,11,15,16,19,20,21,24,27,35],1:[48,49],2:[40,43,46],3:[28,24,31,33],4:[6,25],5:[4,45,47,38,39,50,51],6:[9,12,18,10],7:[3]}
#result_clusters = {0: [4, 35], 1: [10, 6, 32, 18, 17, 24, 2, 7, 11, 0, 13, 19, 1, 23, 26, 9, 34, 38, 40, 41, 45, 44, 47, 3, 5], 2: [12], 3: [14, 8], 4: [16], 5: [20, 22, 36, 48, 42, 46, 39, 30, 31, 21], 6: [25, 49, 27], 7: [28, 15], 8: [33, 29], 9: [43, 37], 10: [50]}
result_clusters = unpickle('new_cluster.txt')#{0: [6,20,21,22,25,30,31,36,37,38,39,42,43,46,48,49,50], 1: [27,40,41], 2: [17,18,24,32], 3: [0,5,9,10,13,19], 4: [1,2,7,8,11,12,15,47], 5: [4,35], 6: [14], 7: [16], 8: [23,26,34], 9: [28,44], 10: [29,33,45]} 
#unpickle('new_cluster.txt')#{0: [6,20,21,22,25,30,31,36,37,38,39,42,43,46,48,49,50], 1: [27,40,41], 2: [17,18,24,32], 3: [0,5,9,10,13,19], 4: [1,2,7,8,11,12,15,47], 5: [4,35], 6: [14], 7: [16], 8: [23,26,34], 9: [28,44], 10: [29,33,45]}
#unpickle('new_cluster.txt')
annotated_clusters = stockmarket_annotated_clusters
# calculate cluster precision
# randomly sample pairs of articles from result_clusters and see if they are in the same annotated_clusters
def cluster_precision(result_clusters, annotated_clusters):
    cp_num = 0.
    cp_den = 0.
    n = 0
    while n < 100000:
        random_result_cluster = random.randint(0,len(result_clusters.keys())-1)
        if len(result_clusters[random_result_cluster]) > 1:
            # choose a pair of articles
            random_article_pair = random.sample(result_clusters[random_result_cluster],2)
            # check if they are in annotated_clusters
            pair_found = 0
            for i in annotated_clusters.values():
                if pair_found==0 and random_article_pair[0] in i and random_article_pair[1] in i:
	            cp_num += 1.
		    cp_den += 1.
		    pair_found = 1
            if pair_found == 0:
	        cp_den+=1
	    n += 1
        #if cp_den != 0:
        #    print "cp: ",cp_num/cp_den
    cp = cp_num/cp_den
    print "cp: ",cp_num/cp_den
    return cp
     
# calculate cluster recall
# randomly sample pairs of articles from annotated_clusters and see if they are in the same result_clusters
def cluster_recall(result_clusters, annotated_clusters):
    cr_num = 0.
    cr_den = 0.
    n = 0
    while n < 100000:
        random_annotated_cluster = random.randint(0,len(annotated_clusters.keys())-1)
        if len(annotated_clusters[random_annotated_cluster]) > 1:
            # choose a pair of articles
            random_article_pair = random.sample(annotated_clusters[random_annotated_cluster],2)
	    pair_found = 0
            # check if they are in annotated_clusters
            for i in result_clusters.values():
                if pair_found == 0 and random_article_pair[0] in i and random_article_pair[1] in i:
                    cr_num += 1.
                    cr_den += 1.
		    pair_found = 1
            if pair_found == 0:
	        cr_den+=1
	    n += 1
    	#if cr_den != 0:
    	#    print "cr: ",cr_num/cr_den
    cr = cr_num/cr_den
    print "cr: ",cr_num/cr_den
    return cr

# calculate clustering f1 measure
def cluster_f1_measure(result_clusters, annotated_clusters):
    cp = cluster_precision(result_clusters, annotated_clusters)
    cr = cluster_recall(result_clusters, annotated_clusters)
    cf = (2.*cp*cr)/(cp+cr)
    print "cf: ",cf
    return cf

def main():
    print cluster_f1_measure(result_clusters, annotated_clusters)

if __name__=='__main__':
    main()
