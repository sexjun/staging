// cpp_xml.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。

#include "tinyxml2_read.h"
#include <../tinyxml2/tinyxml2.h>

#include <iostream>
//#include <tinyxml2.h>
#include <string>

using namespace std;

using namespace tinyxml2;


int loadFile(const char* file_name)
{
    tinyxml2::XMLDocument doc;
    tinyxml2::XMLError ret = doc.LoadFile(file_name);
    if (ret != 0) {
        fprintf(stderr, "fail to load xml file: %s\n", file_name);
        return -1;
    }

    tinyxml2::XMLElement* root = doc.RootElement();
    fprintf(stdout, "root element name: %s\n", root->Name());

    // User
    tinyxml2::XMLElement* user = root->FirstChildElement("User");
    if (!user) {
        fprintf(stderr, "no child element: User\n");
        return -1;
    }
    fprintf(stdout, "user name: %s\n", user->Attribute("Name"));

    tinyxml2::XMLElement* blog = user->FirstChildElement("Blog");
    if (!blog) {
        fprintf(stderr, "no child element: Blog, in User\n");
        return -1;
    }
    fprintf(stdout, "blog value: %s\n", blog->GetText());
    fprintf(stdout, "code value: %s\n\n", user->FirstChildElement("Code")->GetText());

    // Blog
    tinyxml2::XMLElement* blog2 = root->FirstChildElement("Blog");
    if (!blog2) {
        fprintf(stderr, "no child element: Blog\n");
        return -1;
    }
    fprintf(stdout, "blog name: %s\n", blog2->Attribute("Name"));

    tinyxml2::XMLElement* addr = blog2->FirstChildElement("Address");
    if (!addr) {
        fprintf(stderr, "no child element: Address, in Blog\n");
        return -1;
    }
    fprintf(stdout, "address value: %s\n", addr->GetText());
    fprintf(stdout, "id value: %s\n\n", blog2->FirstChildElement("ID")->GetText());

    // Code
    tinyxml2::XMLElement* code = root->FirstChildElement("Code");
    if (!code) {
        fprintf(stderr, "no child element: Code\n");
        return -1;
    }
    fprintf(stdout, "code name: %s\n", code->Attribute("Name"));

    tinyxml2::XMLElement* addr2 = code->FirstChildElement("Address");
    if (!addr2) {
        fprintf(stderr, "no child element: Address, in Code\n");
        return -1;
    }
    fprintf(stdout, "address value: %s\n", addr2->GetText());
    fprintf(stdout, "repositories value: %s\n\n", code->FirstChildElement("Repositories")->GetText());

    return 0;

}

int create_xml_file(const char* file_name)
{
    const char* declaration = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>";

    tinyxml2::XMLDocument doc;
    tinyxml2::XMLError ret = doc.Parse(declaration);
    if (ret != XML_SUCCESS) {
        fprintf(stderr, "fail to parse xml file: %s\n", declaration);
        return FAILD;
    }
    tinyxml2::XMLComment* comment = doc.NewComment("this is a xml test file");
    doc.InsertEndChild(comment);

    tinyxml2::XMLElement* root = doc.NewElement("Root");
    doc.InsertEndChild(root);

    // User
    tinyxml2::XMLElement* user = doc.NewElement("User");
    user->SetAttribute("Name", "fengbingchun");
    root->InsertEndChild(user);

    tinyxml2::XMLElement* blog = doc.NewElement("Blog");
    tinyxml2::XMLText* text1 = doc.NewText("CSDN");
    blog->InsertEndChild(text1);
    user->InsertEndChild(blog);

    tinyxml2::XMLElement* code = doc.NewElement("Code");
    tinyxml2::XMLText* text2 = doc.NewText("GitHub");
    code->InsertEndChild(text2);
    user->InsertEndChild(code);

    // Blog
    tinyxml2::XMLElement* blog2 = doc.NewElement("Blog");
    blog2->SetAttribute("Name", "CSDN");
    root->InsertEndChild(blog2);

    tinyxml2::XMLElement* addr = doc.NewElement("Address");
    tinyxml2::XMLText* text3 = doc.NewText("https://blog.csdn.net/fengbingchun");
    addr->InsertEndChild(text3);
    blog2->InsertEndChild(addr);

    tinyxml2::XMLElement* id = doc.NewElement("ID");
    tinyxml2::XMLText* text4 = doc.NewText("fengbingchun");
    id->InsertEndChild(text4);
    blog2->InsertEndChild(id);

    // Code
    tinyxml2::XMLElement* code2 = doc.NewElement("Code");
    code2->SetAttribute("Name", "GitHub");
    root->InsertEndChild(code2);

    tinyxml2::XMLElement* addr2 = doc.NewElement("Address");
    tinyxml2::XMLText* text5 = doc.NewText("https://github.com//fengbingchun");
    addr2->InsertEndChild(text5);
    code2->InsertEndChild(addr2);

    tinyxml2::XMLElement* repositories = doc.NewElement("Repositories");
    tinyxml2::XMLText* text6 = doc.NewText("27");
    repositories->InsertEndChild(text6);
    code2->InsertEndChild(repositories);
    
    ret = doc.SaveFile(file_name);

}

int main()
{
    const char* file_name = "./tinyxml2/resources/dream_cds.xml";
    //create_xml_file(file_name);
    //loadFile(file_name);
    bool a;
    NewFunction(a);
    return 0;

}

int NewFunction(bool& retflag)
{
    retflag = true;
    string filePath = "./tinyxml2/resources/dream.xml";
    XMLDocument document;
    document.LoadFile(filePath.c_str());
    if (document.ErrorID() != XML_SUCCESS) {
        cout << "load file: " << filePath << "faild" << endl;
        return FAILD;
    }
    //document.Print();

    XMLElement* FM = document.FirstChildElement("PLAY")->FirstChildElement("FM");
    XMLElement* p = FM->FirstChildElement("P");
    while (p)
    {
        cout << p->GetText() << endl;
        p = p->NextSiblingElement();
    }

    //XMLElement* elm2 = elm->FirstChildElement("P");

    //while (elm2->NextSibling())
    //{
    //    cout << elm2->GetText() << endl;
    //}

    //document.SaveFile(filePath.c_str());
    //retflag = false;
    return 0;
}
