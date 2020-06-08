import sys

sys.path.insert(0, '../../../lawpy/')
import lawpy

args = sys.argv


def get_case(casename, cite):
    sess = lawpy.courtlistener()
    fetched = sess.fetch_cases_by_cite(cite)
    filename = "../../unedited/" + casename + ".md"
    try:
        opinion = fetched[0].opinions[0].markdown
        with open(filename, "w") as outfile:
            outfile.write(opinion)
            print("case saved!")
    except:
        print("can't get opinion for cite " + cite)

try:
    casename = args[1]
    cite = args[2]
    get_case(casename, cite)
except:
    print("not enough command line arguments given")

