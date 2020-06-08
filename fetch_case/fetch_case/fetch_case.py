import sys

sys.path.insert(0, '../../../lawpy/')
import lawpy

args = sys.argv


def backup_get_case(filename, cite):
    cap = os.environ["CASELAW"]
    auth = "Token " + cap
    endpoint = "https://api.case.law/v1/cases/"
    try: 
        resp = requests.get(endpoint,
                            headers={"Authorization": auth},
                            params = {"cite": cite, "full_case": True})
        opinion = "\n\n".join([x["text"] for x in resp.json()["results"][0]["casebody"]["data"]["opinions"]])
        with open(filename, "w") as outfile:
            outfile.write(opinion)
            print("case saved!")
    except:
        print("CAP failing too.  Giving up.")


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
        print("courtlistener failed, trying CAP")
        backup_get_case(filename, cite)

try:
    casename = args[1]
    cite = args[2]
    get_case(casename, cite)
except:
    print("not enough command line arguments given")

