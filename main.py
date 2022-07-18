import phenopackets as ph
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.json_format import Parse, MessageToJson
import json
# Creating a patient
# subject = ph.Individual(id="Bob",sex="MALE",date_of_birth=Timestamp(seconds=-123456798))
# Defining the phenotypic features the patient might have
# pheno_features = [ph.PhenotypicFeature(type=ph.OntologyClass(id="HG2G:00001", label="Hoopy"))]
# Combining the phenotypic features with the patient to create a phenopacket
# phenopacket = ph.Phenopacket(id="PPKT:1", subject=subject, phenotypic_features=pheno_features)
#
# test = "test.json"
# with open(test, 'w') as t:
#     Converting the phenopacket to json
#     t.write(MessageToJson(pheno))

with open("test.json", 'r') as jf:
    jtest = json.load(jf)
    for pheno in jtest:
        if pheno["phenotypicFeatures"][0]["type"]["id"]=="HG2G:00001":
            print(pheno["subject"]["id"])
