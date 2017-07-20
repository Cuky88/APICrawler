from subprocess import call

print("\n--- Starting Comparator.jar ---\n")
call('chmod +x test.sh', shell=True)
call("./test.sh")
print("\n--- Comparator.jar finished. Check working directory! ---")