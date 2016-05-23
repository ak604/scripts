version=$1
echo $version

sed -i s/java-[6-8]/java-$version/ ~/.bashrc
sed -i s/java-[6-8]/java-$version/ ~/.bash_profile
sudo sed -i s/java-[6-8]/java-$version/ /etc/environment
update-alternatives --config javac
update-alternatives --config java
