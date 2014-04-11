__author__ = 'kirk'

# this script scrapes data from mich. secretary of state
# elections data pages. only tested on house PRIMARY races
# pages have invalid html w/ data displayed in html tables
# none of the tables have named classes
# so can't beautiful soup based on class name
from bs4 import BeautifulSoup
from urllib2 import urlopen
from collections import OrderedDict

# this scrapes everything for districts 7,9,10,12,13,14
# not tested on any other districts or on years other than 08-12
# returns years grouped by district
# structure: dict(districts):dict(years) :: list(soup[i](beautiful soup)), same for tables...
# rows still include most html tags
def scrape_mi_tables(base_url):
    # orderedDict b/c want to easily reference by key name
    # but also need to preserve order
    districts = OrderedDict([('mi-07','07'), ('mi-09','09'), ('mi-10','10'), ('mi-12','12'), ('mi-13','13'), ('mi-14','14')])
    # districts used here. others not tested
    dist = OrderedDict.fromkeys(['mi-07', 'mi-09', 'mi-10', 'mi-12', 'mi-13', 'mi-14'])
    for a in dist:
        dist[a] = OrderedDict.fromkeys(['06', '08', '10', '12'])  # only these years have been tested
    # create and open url for each district for house PRIMARY elections from 06-12
    # then make soup
    for b in dist:
        for c in dist[b]:
            dist[b][c] = {'url': base_url + c + 'PRI/060' + districts[b] + '000.html'}
    for d in dist:
        for e in dist[d]:
            dist[d][e]['open_url'] = urlopen(dist[d][e]['url'])
    for f in dist:
        for g in dist[f]:
            dist[f][g]['soup'] = BeautifulSoup(dist[f][g]['open_url'])
    # get tables from soup b/c that's where results data is held
    # of course these don't have any class names
    for h in dist:
        for i in dist[h]:
            dist[h][i]['tables'] = dist[h][i]['soup'].findAll('table', {'border': '1'})
            dist[h][i]['tables'] = dist[h][i]['tables'][:len(dist[h][i]['tables']) -1]
            dist[h][i]['rows'] = []
            for j in range(len(dist[h][i]['tables'])):
                dist[h][i]['rows'].append(dist[h][i]['tables'][j].findAll('tr'))
            for k in xrange(0, len(dist[h][i]['rows'])):
                for l in xrange (0, len(dist[h][i]['rows'][k])):
                    dist[h][i]['rows'][k][l] = dist[h][i]['rows'][k][l].contents
            # only want data in last 4 rows
            for m in xrange(len(dist[h][i]['rows'])):
                dist[h][i]['rows'][m] = dist[h][i]['rows'][m][len(dist[h][i]['rows'][m]) - 4:]
                for n in xrange(len(dist[h][i]['rows'][m])):
                    for o in xrange(len(dist[h][i]['rows'][m][n])):
                        dist[h][i]['rows'][m][n][o] = dist[h][i]['rows'][m][n][o].contents
    return dist


# this adds list of candidates running for primaries in both parties for years 08-12
# for each district
# designed to use output from scrape_mi_tables
def get_names (dist):
    # check notes
# this adds partisan affiliation to candidates in primary races
# requires output from get_names
def get_party (dist):
    # check notes

# this gets final official results from each primary
# and calculates margin of victory
def get_results (dist):
    # check notes



















