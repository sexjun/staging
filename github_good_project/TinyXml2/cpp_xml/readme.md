# learing tinyxml



### 1. env

- add inlude path for vs

![image-20210925004046675](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210925004046.png)



- get  tinyxml2 code 

```c
git clone git@github.com:leethomason/tinyxml2.git
```



### 2. tinyxml2 

- include header

```
#include <tinyxml2.h>
using namespace tinyxml2;
```

#### 2.1 加载xml

- 从文件中加载xml

```c
    XMLDocument document;
    document.LoadFile("resources/dream.xml");
```



- 从内存中加载xml

```c
    static const char* xml =
        "<?xml version=\"1.0\"?>"
        "<!DOCTYPE PLAY SYSTEM \"play.dtd\">"
        "<PLAY>"
        "<TITLE>A Midsummer Night's Dream</TITLE>"
        "</PLAY>";

    XMLDocument doc;
    doc.Parse(xml);
```

#### 2.2 获取元素

`doc.FirstChildElement()`可以有效的跳过xml的声明和dtd

```c
    XMLElement* titleElement = doc.FirstChildElement("PLAY")->FirstChildElement("TITLE");
    const char* title = titleElement->GetText();
```

查询元素的值：

```xml
        <information>
        	<attributeApproach v='2' />
        	<textApproach>
        		<v>2</v>
        	</textApproach>
        </information>
```



- 通过

` attributeApproachElement->QueryIntAttribute(属性建值, &v0);`

` textApproachElement->FirstChildElement("v")->QueryIntText(&v1);`

```c
    XMLElement* attributeApproachElement = doc.FirstChildElement()->FirstChildElement("attributeApproach");
    attributeApproachElement->QueryIntAttribute("v", &v0);

    XMLElement* textApproachElement = doc.FirstChildElement()->FirstChildElement("textApproach");
    textApproachElement->FirstChildElement("v")->QueryIntText(&v1);
```

#### 2.3 给元素新加属性



这里有很多的重载方法

```c
/// Sets the named attribute to value.
    void SetAttribute( const char* name, const char* value )	{
        XMLAttribute* a = FindOrCreateAttribute( name );
        a->SetAttribute( value );
    }
    /// Sets the named attribute to value.
    void SetAttribute( const char* name, int value )			{
        XMLAttribute* a = FindOrCreateAttribute( name );
        a->SetAttribute( value );
    }
    /// Sets the named attribute to value.
    void SetAttribute( const char* name, unsigned value )		{
        XMLAttribute* a = FindOrCreateAttribute( name );
        a->SetAttribute( value );
    }

	/// Sets the named attribute to value.
	void SetAttribute(const char* name, int64_t value) {
		XMLAttribute* a = FindOrCreateAttribute(name);
		a->SetAttribute(value);
	}

    /// Sets the named attribute to value.
    void SetAttribute(const char* name, uint64_t value) {
        XMLAttribute* a = FindOrCreateAttribute(name);
        a->SetAttribute(value);
    }

    /// Sets the named attribute to value.
    void SetAttribute( const char* name, bool value )			{
        XMLAttribute* a = FindOrCreateAttribute( name );
        a->SetAttribute( value );
    }
    /// Sets the named attribute to value.
    void SetAttribute( const char* name, double value )		{
        XMLAttribute* a = FindOrCreateAttribute( name );
        a->SetAttribute( value );
    }
    /// Sets the named attribute to value.
    void SetAttribute( const char* name, float value )		{
        XMLAttribute* a = FindOrCreateAttribute( name );
        a->SetAttribute( value );
    }

```



```c
实际使用：
    elm->SetAttribute("test", 0);
```

![image-20210925013545197](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210925013545.png)

#### 2.4 删除元素属性

```c
    /**
    	Delete an attribute.
    */
    void DeleteAttribute( const char* name );
```



![image-20210925013617900](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210925013617.png)

#### 2.5 获取元素尖括号里的数值

```c
    XMLError QueryIntText( int* ival ) const;
    /// See QueryIntText()
    XMLError QueryUnsignedText( unsigned* uval ) const;
	/// See QueryIntText()
	XMLError QueryInt64Text(int64_t* uval) const;
	/// See QueryIntText()
	XMLError QueryUnsigned64Text(uint64_t* uval) const;
	/// See QueryIntText()
    XMLError QueryBoolText( bool* bval ) const;
    /// See QueryIntText()
    XMLError QueryDoubleText( double* dval ) const;
    /// See QueryIntText()
    XMLError QueryFloatText( float* fval ) const;
```







## 源码

源码学习方法分享：

1. 看readme
2. 看test案例
3. 看头文件类的方法





tinyxml2里面有几个比较重要的对象，分别是：

1. 文档
2. 键值对
3. 元素



单个元素最大复杂深度限制：

```c
// A fixed element depth limit is problematic. There needs to be a
// limit to avoid a stack overflow. However, that limit varies per
// system, and the capacity of the stack. On the other hand, it's a trivial
// attack that can result from ill, malicious, or even correctly formed XML,
// so there needs to be a limit in place.
static const int TINYXML2_MAX_ELEMENT_DEPTH = 100;
```

重要的类：

```c
/** A Document binds together all the functionality.
	It can be saved, loaded, and printed to the screen.
	All Nodes are connected and allocated to a Document.
	If the Document is deleted, all its Nodes are also deleted.
*/
class XMLDocument;
/** The element is a container class. It has a value, the element name,
	and can contain other elements, text, comments, and unknowns.
	Elements also contain an arbitrary number of attributes.
*/
class XMLElement;
/** An attribute is a name-value pair. Elements have an arbitrary
	number of attributes, each with a unique name.

	@note The attributes are not XMLNodes. You may only query the
	Next() attribute in a list.
*/
class XMLAttribute;

class XMLComment;
class XMLText;
class XMLDeclaration;
class XMLUnknown;
class XMLPrinter;

XMLNode是一个重要的基类
     XMLNode is a base class for every object that is in the
	XML Document Object Model (DOM), except XMLAttributes.
class TINYXML2_LIB XMLNode{
         // 上一个节点
             const XMLNode*	PreviousSibling() const					{
        return _prev;
                 
                 const XMLElement*	PreviousSiblingElement( const char* name = 0 ) const ;
    }
     }


	@verbatim
	A Document can contain:	Element	(container or leaf)
							Comment (leaf)
							Unknown (leaf)
							Declaration( leaf )

	An Element can contain:	Element (container or leaf)
							Text	(leaf)
							Attributes (not on tree)
							Comment (leaf)
							Unknown (leaf)
```



- XMLDocument

```c++
class TINYXML2_LIB XMLDocument : public XMLNode
{
    XMLError Parse( const char* xml, size_t nBytes=static_cast<size_t>(-1) );
    XMLError LoadFile( const char* filename );
    // open as "rb" and need user open file and close file.
    XMLError LoadFile( FILE* );
    XMLError SaveFile( const char* filename, bool compact = false );
    // need user to open file with "rb" mode and close the file
    XMLError SaveFile( FILE* fp, bool compact = false );
    
    
    void Print( XMLPrinter* streamer=0 ) const;
    
    
    void DeleteNode( XMLNode* node );
}
```

- XMLAttribute

1. name-value pair
2. Elements have an arbitrary

```c++
class TINYXML2_LIB XMLAttribute
{
    const char* Name() const;
    const char* Value() const;
    int GetLineNum() const { return _parseLineNum; }
    // 查询值，带有安全保护。 成功返回：XML_SUCCESS 失败：XML_WRONG_ATTRIBUTE_TYPE
    XMLError QueryIntValue( int* value ) const;
    /// See QueryIntValue
    XMLError QueryUnsignedValue( unsigned int* value ) const;
	/// See QueryIntValue
	XMLError QueryInt64Value(int64_t* value) const;
    /// See QueryIntValue
    XMLError QueryUnsigned64Value(uint64_t* value) const;
	/// See QueryIntValue
    XMLError QueryBoolValue( bool* value ) const;
    /// See QueryIntValue
    XMLError QueryDoubleValue( double* value ) const;
    /// See QueryIntValue
    XMLError QueryFloatValue( float* value ) const;

    // 
    /// Set the attribute to a string value.
    void SetAttribute( const char* value );
    /// Set the attribute to value.
    void SetAttribute( int value );
    /// Set the attribute to value.
    void SetAttribute( unsigned value );
	/// Set the attribute to value.
	void SetAttribute(int64_t value);
    /// Set the attribute to value.
    void SetAttribute(uint64_t value);
    /// Set the attribute to value.
    void SetAttribute( bool value );
    /// Set the attribute to value.
    void SetAttribute( double value );
    /// Set the attribute to value.
    void SetAttribute( float value );
}
```

- XMLElement

```c++
class TINYXML2_LIB XMLElement : public XMLNode
{
        const char* Name() const		{
        return Value();
    }
        void SetName( const char* str, bool staticMem=false )	{
        SetValue( str, staticMem );
    }
        const char* Attribute( const char* name, const char* value=0 ) const;
}
```

