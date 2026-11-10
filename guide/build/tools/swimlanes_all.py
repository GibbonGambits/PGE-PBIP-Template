import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from swimlane import swimlane
os.chdir('/home/user/PGE-PBIP-Template/guide/images')
L=[("You","you"),("VS Code","n"),("AI agent","ai"),("Git (your PC)","g")]
swimlane('03-4-swimlane-build',L,[(0,1,"Open the repo folder in VS Code"),(3,2,"Create a branch: git checkout -b feature/x"),(0,3,"Ask the agent: build the page in specs/x.md"),(2,4,"Edit the report and model files"),(2,5,"Run the checks, show screenshots, report"),(1,6,"You review every change in Source Control")])
L2=[("You","you"),("Git (your PC)","g"),("GitHub","ext")]
swimlane('03-5-swimlane-share',L2,[(1,7,"Stage + commit with a clear message"),(1,8,"git push uploads your branch"),(2,9,"You open a pull request"),(2,10,"CODEOWNERS reviewers are asked to review"),(0,11,"You fix any review comments"),(2,12,"Reviewer approves; branch is merged")])
swimlane('05-4-swimlane-plan-build',[("You","you"),("AI agent","ai"),("Scripts","r")],[
 (0,1,"Open the repo and create a branch"),(2,2,"Session brief prints the rules and bridge status"),(0,3,"Copy specs/TEMPLATE.md and fill in the spec"),(1,4,"Read the rule files, matching skills and the spec"),(1,5,"Write the model (TMDL), then the report (PBIR)"),(2,6,"Write guard + validate hook check each file")])
swimlane('05-5-swimlane-check',[("AI agent","ai"),("Scripts","r"),("Power BI Desktop","ext"),("You","you")],[
 (1,7,"validate-json, validate-pbip, Test-PbipSemantics"),(0,8,"Fix any errors they report"),(1,9,"Invoke-PbipVerify.ps1 -Mode Review"),(2,10,"Reload through the Desktop Bridge"),(2,11,"Screenshot every page"),(1,12,"Hand back PNGs, page names, status"),(0,13,"Review PNGs, report findings by page name"),(3,14,"Read the findings and screenshots")])
swimlane('05-6-swimlane-share',[("You","you"),("Git","g"),("GitHub","ext")],[
 (0,15,"Review the changes in Source Control"),(1,16,"Commit, then push the branch"),(2,17,"Pull request reviewed, merged to dev, then test"),(2,18,"ai-testing.yml runs on the test branch"),(0,19,"Download the test results artifact")])
swimlane('11-3-actions-swimlane',[("You","you"),("GitHub","ext"),("Runner (cloud PC)","r"),("AI model service","ai")],[
 (0,1,"Merge a pull request into the test branch"),(1,2,"Sees the push; starts the workflow"),(2,3,"Checks out the code and runs the validators"),(2,4,"run-ai-md-test.ps1 sends the prompt and files"),(3,5,"Returns a markdown test report"),(2,6,"Saves tests/results/ and uploads the artifact"),(1,7,"Shows the run result and the artifact"),(0,8,"Download and read test_results.md")])
