#=========ex1========

required_packages={"python3", "pip","requests", "boto3","pip"}

#=========ex2========

#? print(required_packages)

#=========ex3=======

#? print("is requests", "requests" in required_packages) 

#=========ex4=======

#? print("is ansible", "ansible" in required_packages )

#=========ex5=======

#? print(f"Is 'requests' required? {'requests' in required_packages}")

#=========ex6=======

#? print(f"is ansible required ? {"ansible" in required_packages}")

#=========ex7=======

required_packages.add("paramiko")

#=========ex8=======

required_packages.remove("pip")

#=========ex9=======

#? print(required_packages)

#=========ex10======

installed_packages={"docker", "python3", "pip"}

#==========ex11=====

missing_packages= required_packages - installed_packages

#? print(missing_packages)

#=========ex12========

extra_packages = installed_packages - required_packages
#? print(extra_packages)

#=========ex13========

common_packages = required_packages & installed_packages
#? print(common_packages)

#==========ex14======
print(f" all the packages requierd{required_packages} installed {installed_packages} missing {missing_packages} and common {common_packages}")
