import nbformat
with open("notebook\kaggleint3 - Copy - Copy.ipynb","r") as file:
    notebook=nbformat.read(file, as_version=4)
# print(x)
target_cell_index = 9  # Replace with the actual index of the target code cell

# Access the code cell
code_cell = notebook.cells[target_cell_index]
id="123456789"
data="""up and remove the resources you previously set up in the Kubernetes cluster.
These steps cover the creation of a deployment in Minikube, managing pods with
replicas, and optionally exposing the deployment as a service for external access. Adjust
the configuration based on your specific application needs.


 KR21 SOFTWARE ENGINEERING CSE/IT/CSM/CSD III/I
1SOFTWARE ENGINEERING
UNIT – 4
CHAPTER – 4
CONTINUOUS MONITORING USING NAGIOS
I. UNDERSTANDING CONTINUOUS MONITORING
Continuous monitoring in DevOps refers to the practice of keeping a close and constant eye on the
various aspects of software development and operations throughout the entire development
lifecycle. It involves continuously gathering and analyzing data to ensure that the software is
performing well, meeting security standards, and delivering value to users.
It involves:
Constant Observation: Continuous monitoring means consistently observing and collecting data
about the software development and operation processes. This includes tracking code changes,
system performance, and user interactions.
Automation: Automation plays a key role in continuous monitoring. Automated tools are used to
collect data, run tests, and perform various checks on the software. This helps in quickly
identifying issues and trends without manual intervention.
Feedback Loop : Continuous monitoring creates a feedback loop, providing information to
development and operations teams in real-time or near-real-time. This allows teams to react
promptly to any issues, make improvements, and iterate on the software more rapidly.
Security Monitoring: It also involves monitoring for security vulnerabilities and threats. This
ensures that the software is protected against potential security risks, and any vulnerabilities are
identified and addressed promptly.
Performance Monitoring: Continuous monitoring includes keeping an eye on the performance
of the software. This involves tracking response times, resource usage, and other performance
metrics to ensure that the application is running efficiently.KR21 SOFTWARE ENGINEERING CSE/IT/CSM/CSD III/I
2User Experience Monitoring: Monitoring user interactions and feedback helps in understanding
how users are experiencing the software. This information can be valuable for making user-centric
improvements.
Compliance Monitoring: Ensuring that the software complies with relevant standards,
regulations, and best practices is another aspect of continuous monitoring. This is crucial for
industries with strict compliance requirements.
Continuous monitoring in DevOps is about staying vigilant throughout the entire software
development lifecycle, using automated tools to collect and analyze data, and ensuring that the
software is secure, performs well, and meets the needs of users. It helps teams to identify and
address issues early, promoting a more efficient and reliable development process.
II. NEED OF CONTINUOUS MONITORING
"""
code_cell['source'] += f'id = "{id}"\ntext = """{data}"""'
# data=data.replace("\n","\\n")
# x=x.replace('id=\\n',f'id=\\"{id}\\"',1)
# x=x.replace('data=',f'data=\\"\\"\\"{data}\\"\\"\\"',1)
# # print(x)
with open("notebook\kaggleint3.ipynb","w") as file:
    nbformat.write(notebook, file)