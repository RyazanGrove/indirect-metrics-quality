column_names = [
"Date",	"Tag", "Total Cyclomatic Complexity", "Files for Cyclomatic Complexity", 
"Average Cyclomatic Complexity per file", "Total Maintainability Index", "Files for Maintainability Index",
"Average Maintainability Index per file", "Total Halstead Volume", "Files for Halstead Volume",
"Average Halstead Volume per file", "Total Lines of Code (raw analysis)", "Average Lines of Code (raw analysis) per file",
"Total percentage of comments (raw analysis)", "Average percentage of comments (raw analysis) per file", "Files for raw code analysis"
]

operational_metrics_names = ["Static tests", "Dynamic tests", "Integration tests",
                             "End-to-end tests", "Test Pass Rate", "Build related",
                             "Pipeline Pass Rate", "Security scan", "Code quality scan"]

verification_start_date = '2023-09-13'
verification_end_date = '2023-09-27'

services_metadata = {
    "operational": [
        { "service": "S1", "sheet_name": "1 rt-orchestration-service", "metrics": [operational_metrics_names[i] for i in [0,1,2,4,5,6,7]]},
        { "service": "S2", "sheet_name": "2 rt-image2plan-ui-lib", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,7,8]]},
        { "service": "S3", "sheet_name": "3 rt-auth-service", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,7]]},
        { "service": "S4", "sheet_name": "4 rt-dicom-comm-service", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,7]]},
        { "service": "S5", "sheet_name": "5 rt-image2plan-config-editor-s", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,7]]},
        { "service": "S6", "sheet_name": "6 rt-image2plan-infra-service", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,7,8]]},
        { "service": "S7", "sheet_name": "7 rt-opentext-etx-service", "metrics": [operational_metrics_names[i] for i in [5,6]]},
        { "service": "S8", "sheet_name": "8 rt-remote-desktop-service", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,7]]},
        { "service": "S9", "sheet_name": "9 rt-bdd-ui-test-lib", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,8]]},
        { "service": "S10", "sheet_name": "10 rt-bdd-api-test-lib", "metrics": [operational_metrics_names[i] for i in [0,1,4,5,6,8]]},
        { "service": "S11", "sheet_name": "11 rt-orchestrator-e2e-testing", "metrics": [operational_metrics_names[i] for i in [3,4,5,6]]},
    ]
}