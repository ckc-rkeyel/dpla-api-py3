# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from dpla_api import DplaApi
da = DplaApi()
da.search("crochet* OR knit*", page_size=500)
da.build_arc_rdf_dataset()
da.create_tsv(output_path="data/ckc.txt")

