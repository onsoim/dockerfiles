if [ $# -ne 2 ]
then
	echo "Usage: Sign.sh old_name new_name"
else
	echo "$1 is now being signed and will be renamed to $2"
	java -jar signapk.jar testkey.x509.pem testkey.pk8 ../apk/$1 ../apk/$2
	echo "Signing Complete"
fi