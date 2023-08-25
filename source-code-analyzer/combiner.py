import pandas as pd

from bugs_calculator import get_bugs_dict


service2 = pd.read_excel('data\\Masters thesis draft 1.2 with demos.xlsx', sheet_name="1 rt-orchestration-service")
### demos
service1 = service2[service2["Demo"] == 1]

### demos
service1["Week"] = service1["Date"].dt.isocalendar().week
service1["Year"] = service1["Date"].dt.isocalendar().year
service1["Danger"] = 0

#print(service1.info())

bugs_dict = get_bugs_dict()

for index, row in service1.iterrows():
    #print(row)
    if (row['Year'] == 2022):
        if(row['Week'] in bugs_dict["2022"]):
            service1.loc[index, 'Danger'] = bugs_dict["2022"][row['Week']]

    if (row['Year'] == 2023):
        if(row['Week'] in bugs_dict["2023"]):
            service1.loc[index, 'Danger'] = bugs_dict["2023"][row['Week']]


#service2022 = service1.loc[service1["Year"] == 2023]
#print(service2022)
#print(service1.info())
#print(service1[50:80])

pipeline_pass_rate = service1[["Pipeline Pass Rate", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
print("Pipeline pass rate correlation = ",pipeline_pass_rate["Pipeline Pass Rate"].corr(pipeline_pass_rate["Danger"]))

test_pass_rate = service1[["Test Pass Rate", "Danger"]].loc[service1["Test Pass Rate"].notna()]
print("Tests pass rate correlation = ",test_pass_rate["Test Pass Rate"].corr(test_pass_rate["Danger"]))

#Static and Dynamic Tests\Static Tests
static_tes_pass_rate = service1[["Pipeline Pass Rate", "Static and Dynamic Tests\Static Tests", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
static_tes_pass_rate["Static and Dynamic Tests\Static Tests"] = static_tes_pass_rate["Static and Dynamic Tests\Static Tests"].fillna(0)
#print(static_tes_pass_rate[90:110])
print("Static and Dynamic Tests\Static Tests correlation = ",static_tes_pass_rate["Static and Dynamic Tests\Static Tests"].corr(static_tes_pass_rate["Danger"]))

#Static and Dynamic Tests\Dynamic Tests
dynamic_tes_pass_rate = service1[["Pipeline Pass Rate", "Static and Dynamic Tests\Dynamic Tests", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
dynamic_tes_pass_rate["Static and Dynamic Tests\Dynamic Tests"] = dynamic_tes_pass_rate["Static and Dynamic Tests\Dynamic Tests"].fillna(0)
print("Static and Dynamic Tests\Dynamic Tests correlation = ",dynamic_tes_pass_rate["Static and Dynamic Tests\Dynamic Tests"].corr(dynamic_tes_pass_rate["Danger"]))

#Veracode Scans\Security regression test against baseline
veracode_scan_security_pass_rate = service1[["Pipeline Pass Rate", "Veracode Scans\Security regression test against baseline", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
veracode_scan_security_pass_rate["Veracode Scans\Security regression test against baseline"] = veracode_scan_security_pass_rate["Veracode Scans\Security regression test against baseline"].fillna(0)
print("Veracode Scans\Security regression test against baseline correlation = ",veracode_scan_security_pass_rate["Veracode Scans\Security regression test against baseline"].corr(veracode_scan_security_pass_rate["Danger"]))

#Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results
veracode_scan_create_pass_rate = service1[["Pipeline Pass Rate", "Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
veracode_scan_create_pass_rate["Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results"] = veracode_scan_create_pass_rate["Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results"].fillna(0)
print("Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results correlation = ",veracode_scan_create_pass_rate["Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results"].corr(veracode_scan_create_pass_rate["Danger"]))

#Build Service Packages\Build distributed container
build_service_build_container_pass_rate = service1[["Pipeline Pass Rate", "Build Service Packages\Build distributed container", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
build_service_build_container_pass_rate["Build Service Packages\Build distributed container"] = build_service_build_container_pass_rate["Build Service Packages\Build distributed container"].fillna(0)
print("Build Service Packages\Build distributed container correlation = ",build_service_build_container_pass_rate["Build Service Packages\Build distributed container"].corr(build_service_build_container_pass_rate["Danger"]))

#TMA S
tma_s_pass_rate = service1[["Pipeline Pass Rate", "TMA S", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
tma_s_pass_rate["TMA S"] = tma_s_pass_rate["TMA S"].fillna(0)
print("TMA S correlation = ",tma_s_pass_rate["TMA S"].corr(tma_s_pass_rate["Danger"]))

#TMA C
tma_c_pass_rate = service1[["Pipeline Pass Rate", "TMA C", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
tma_c_pass_rate["TMA C"] = tma_c_pass_rate["TMA C"].fillna(0)
print("TMA C correlation = ",tma_c_pass_rate["TMA C"].corr(tma_c_pass_rate["Danger"]))

#Veracode Scan \ Generate requirements.txt file
veracode_scan_generate_pass_rate = service1[["Pipeline Pass Rate", "Veracode Scan \ Generate requirements.txt file", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
veracode_scan_generate_pass_rate["Veracode Scan \ Generate requirements.txt file"] = veracode_scan_generate_pass_rate["Veracode Scan \ Generate requirements.txt file"].fillna(0)
print("Veracode Scan \ Generate requirements.txt file correlation = ",veracode_scan_generate_pass_rate["Veracode Scan \ Generate requirements.txt file"].corr(veracode_scan_generate_pass_rate["Danger"]))

#Determine Git Version\Determine SemVer
determine_git_pass_rate = service1[["Pipeline Pass Rate", "Determine Git Version\Determine SemVer", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
determine_git_pass_rate["Determine Git Version\Determine SemVer"] = determine_git_pass_rate["Determine Git Version\Determine SemVer"].fillna(0)
print("Determine Git Version\Determine SemVer correlation = ",determine_git_pass_rate["Determine Git Version\Determine SemVer"].corr(determine_git_pass_rate["Danger"]))

#Integration Tests\Integration Tests
integration_tests_pass_rate = service1[["Pipeline Pass Rate", "Integration Tests\Integration Tests", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
integration_tests_pass_rate["Integration Tests\Integration Tests"] = integration_tests_pass_rate["Integration Tests\Integration Tests"].fillna(0)
print("Integration Tests\Integration Tests correlation = ",integration_tests_pass_rate["Integration Tests\Integration Tests"].corr(integration_tests_pass_rate["Danger"]))

#Build Service Packages\Build a wheel
build_service_build_wheel_pass_rate = service1[["Pipeline Pass Rate", "Build Service Packages\Build a wheel", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
build_service_build_wheel_pass_rate["Build Service Packages\Build a wheel"] = build_service_build_wheel_pass_rate["Build Service Packages\Build a wheel"].fillna(0)
print("Build Service Packages\Build a wheel correlation = ",build_service_build_wheel_pass_rate["Build Service Packages\Build a wheel"].corr(build_service_build_wheel_pass_rate["Danger"]))

#Static and Dynamic Tests\PublishCodeCoverageResults
publish_code_coverage_pass_rate = service1[["Pipeline Pass Rate", "Static and Dynamic Tests\PublishCodeCoverageResults", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
publish_code_coverage_pass_rate["Static and Dynamic Tests\PublishCodeCoverageResults"] = publish_code_coverage_pass_rate["Static and Dynamic Tests\PublishCodeCoverageResults"].fillna(0)
print("Static and Dynamic Tests\PublishCodeCoverageResults correlation = ",publish_code_coverage_pass_rate["Static and Dynamic Tests\PublishCodeCoverageResults"].corr(publish_code_coverage_pass_rate["Danger"]))

#Veracode Scans\Veracode Sandbox Scan
veracode_scan_sandbox_pass_rate = service1[["Pipeline Pass Rate", "Veracode Scans\Veracode Sandbox Scan", "Danger"]].loc[service1["Pipeline Pass Rate"].notna()]
veracode_scan_sandbox_pass_rate["Veracode Scans\Veracode Sandbox Scan"] = veracode_scan_sandbox_pass_rate["Veracode Scans\Veracode Sandbox Scan"].fillna(0)
print("Veracode Scans\Veracode Sandbox Scan correlation = ",veracode_scan_sandbox_pass_rate["Veracode Scans\Veracode Sandbox Scan"].corr(veracode_scan_sandbox_pass_rate["Danger"]))

service_to_print = service1[["Pipeline Pass Rate", "Static and Dynamic Tests\Static Tests",
                              "Static and Dynamic Tests\Dynamic Tests",
                                "Veracode Scans\Security regression test against baseline", 
                                "Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results", 
                                "Build Service Packages\Build distributed container", 
                                "TMA S",
                                "TMA C", 
                                "Veracode Scan \ Generate requirements.txt file", 
                                "Determine Git Version\Determine SemVer",
                                "Integration Tests\Integration Tests",
                                "Build Service Packages\Build a wheel",
                                "Static and Dynamic Tests\PublishCodeCoverageResults",
                                "Veracode Scans\Veracode Sandbox Scan",
                                "Danger"
                            ]]
#service_to_print
service_to_print["Static and Dynamic Tests\Static Tests"].fillna(0,inplace=True) # = service_to_print["Static and Dynamic Tests\Static Tests"].fillna(0)
service_to_print["Static and Dynamic Tests\Dynamic Tests"].fillna(0,inplace=True) # = service_to_print["Static and Dynamic Tests\Dynamic Tests"].fillna(0)
service_to_print["Veracode Scans\Security regression test against baseline"].fillna(0,inplace=True) # = service_to_print["Veracode Scans\Security regression test against baseline"].fillna(0)
service_to_print["Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results"].fillna(0,inplace=True) # = service_to_print["Veracode Scans\Create Build Artifact for Veracode Pipeline Scan Results"].fillna(0)
service_to_print["Build Service Packages\Build distributed container"].fillna(0,inplace=True) # = service_to_print["Build Service Packages\Build distributed container"].fillna(0)
service_to_print["TMA S"].fillna(0,inplace=True) # = service_to_print["TMA S"].fillna(0)
service_to_print["TMA C"].fillna(0,inplace=True) # = service_to_print["TMA C"].fillna(0)
service_to_print["Veracode Scan \ Generate requirements.txt file"].fillna(0,inplace=True) # = service_to_print["Veracode Scan \ Generate requirements.txt file"].fillna(0)
service_to_print["Determine Git Version\Determine SemVer"].fillna(0,inplace=True) # = service_to_print["Determine Git Version\Determine SemVer"].fillna(0)
service_to_print["Integration Tests\Integration Tests"].fillna(0,inplace=True) # = service_to_print["Integration Tests\Integration Tests"].fillna(0)
service_to_print["Build Service Packages\Build a wheel"].fillna(0,inplace=True) # = service_to_print["Build Service Packages\Build a wheel"].fillna(0)
service_to_print["Static and Dynamic Tests\PublishCodeCoverageResults"].fillna(0,inplace=True) # = service_to_print["Static and Dynamic Tests\PublishCodeCoverageResults"].fillna(0)
service_to_print["Veracode Scans\Veracode Sandbox Scan"].fillna(0,inplace=True) # = service_to_print["Veracode Scans\Veracode Sandbox Scan"].fillna(0)
service_to_print_excel = service_to_print.loc[service_to_print["Pipeline Pass Rate"].notna()]

service_to_print_excel.to_excel('out\\test.xlsx')
"""
from bugs_formater import get_2022_dict

bugs_2022 = get_2022_dict()

print(bugs_2022)

data = pd.read_excel('data\\Masters thesis draft 1.0.xlsx')
data = data[40:100]
data["Week"] = data["Date"].dt.isocalendar().week
data["Year"] = data["Date"].dt.isocalendar().year
data["Danger"] = 0

print(data.info())
for index, row in data.iterrows():
    #print(row)
    if (row['Year'] == 2022):
        if(row['Week'] in bugs_2022):
            #row["Danger"] = bugs_2022[row['Week']]
            #print(row['Week'])
            #data.at['Danger', index] = bugs_2022[row['Week']]
            data.loc[index, 'Danger'] = bugs_2022[row['Week']]

#print(data.loc[data["Danger"] != 0])
#print(data['Danger'])
data = data.dropna(axis=0, subset=["Paas Rate"])


print("Paas Rate",data["Paas Rate"].corr(data["Danger"]))
#print(data)
#print("Test pass rate",data["Test pass rate"].corr(data["Danger"]))
"""