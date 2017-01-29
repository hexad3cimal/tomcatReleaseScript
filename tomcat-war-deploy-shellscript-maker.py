
"""
*** This script creates a shell script which helps(helped me) in deploying the war file after each build,
    if you are not using any CI tools ***
"""

file_name= input("Enter shell script name: ")
tomcat_home =  input("Enter tomcat home folder (with trailing slash): ")
war_location =  input("Enter war location: ")




shellScriptFile = open(file_name+".sh", 'w')
shellScriptFile.write("sh "+tomcat_home+"bin/catalina.sh stop\n")
shellScriptFile.write("rm -rf "+tomcat_home+"webapps/*\n")
shellScriptFile.write("rm -rf "+tomcat_home+"work/*\n")
shellScriptFile.write("cp "+war_location+" "+tomcat_home+"webapps/\n")
shellScriptFile.write("sh "+tomcat_home+"bin/catalina.sh start\n")

shellScriptFile.close()

