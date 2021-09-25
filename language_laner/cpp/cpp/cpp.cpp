// cpp.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <string>

using namespace std;

void test02()
{
	//替换
	string str1 = "abcdefgde";
	str1.replace(1, 3, "1111");

	cout << "str1 = " << str1 << endl;
}

void test01()
{

	string str = "abcdefg";
	string subStr = str.substr(1, 3);
	cout << "subStr = " << subStr << endl;

	string email = "hello@sina.com";
	int pos = email.find("@");
	cout << pos << endl;
	string username = email.substr(0, pos);
	string username1 = email.substr(0, 5);
	cout << "username: " << username << endl;
	cout << "username1: " << username1 << endl;

}

int main()
{
	test01();
    std::cout << "Hello World!\n";
}