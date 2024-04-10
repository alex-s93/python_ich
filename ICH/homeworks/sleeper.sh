# 1
echo "# 1 - write time info:" >> "$file"
for i in {1..10}
do
	date "+%H:%M:%S" >> "$file"
	# 2
	sleep 2
done
echo "_______________________________________" >> "$file"

# 3
echo "# 3 - processor info:" >> "$file"
cat /proc/cpuinfo | grep "model name" | cut -d':' -f 2 >> "$file"
echo "_______________________________________" >> "$file"

# 4
echo "# 4 - write operation system name:" >> "$file"
cat /etc/os-release | grep -w "NAME" >> "$file"
echo "_______________________________________" >> "$file"

# 5
echo "# 5 - write operation system name without 'NAME' key:" >> "$file"
cat /etc/os-release | grep -w "NAME" | cut -d'=' -f 2 >> "$file"
echo "_______________________________________" >> "$file"

# 6
echo "# 6 - create 50 files:" >> "$file"
mkdir -p $path/50_files
for i in {50..100}
do
	touch $path/50_files/$i.txt
done
echo "50 files successfully created" >> "$file"
echo "_______________________________________" >> "$file"