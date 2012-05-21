from xml.dom.minidom import Document
import string

def XMLify(*args, **kwargs):
    doc = Document()
    parent = doc.createElement('slotmogul')
    doc.appendChild(parent)
    for keyword,keyvalue in kwargs.iteritems():
        try:#if is a list of stuff
            for i,value in enumerate(keyvalue):
                if i == 0:
                    nodelabelparent = doc.createElement(keyword)
                    parent.appendChild(nodelabelparent)
                nodelabel = doc.createElement(str(type(value))[str(type(value)).index('\'')+1:str(type(value)).rindex('\'')])\
                        if not string.rfind(str(type(value)),'.') else\
                        doc.createElement(str(type(value))[str(type(value)).rindex('.')+1:str(type(value)).rindex('\'')])
                nodelabelparent.appendChild(nodelabel)
                try:#if is a class
                    for attr, attrvalue in value.__dict__.iteritems():
                        if not str(attr).startswith('_'):
                            nodelabelchild = doc.createElement(attr)
                            nodelabel.appendChild(nodelabelchild)
                            nodevalue = doc.createTextNode(str(attrvalue))
                            nodelabelchild.appendChild(nodevalue)
                except:#not a class
                    try:#if it is a dictionary
                        for attr, attrvalue in value.iteritems():
                            if not str(attr).startswith('_'):
                                nodelabelchild = doc.createElement(attr)
                                nodelabel.appendChild(nodelabelchild)
                                nodevalue = doc.createTextNode(str(attrvalue))
                                nodelabelchild.appendChild(nodevalue)
                    except:#if it is just an it or something
                        nodevalue = doc.createTextNode(str(value))
                        nodelabel.appendChild(nodevalue)
        except:#if it is a single object
            try:#if the object is a class
                for i,attr_attrvalue in enumerate(keyvalue.__dict__.iteritems()):
                    if i == 0:
                        nodelabelparent = doc.createElement(keyword)
                        parent.appendChild(nodelabelparent)
                    if not str(attr_attrvalue[0]).startswith('_'):
                        nodelabel = doc.createElement(attr_attrvalue[0])
                        nodelabelparent.appendChild(nodelabel)
                        nodevalue = doc.createTextNode(str(attr_attrvalue[1]))
                        nodelabel.appendChild(nodevalue)
            except:#if the object is just an int or something
                nodelabel = doc.createElement(keyword)
                parent.appendChild(nodelabel)
                nodevalue = doc.createTextNode(str(keyvalue))
                nodelabel.appendChild(nodevalue)
    return doc.toprettyxml(indent="  ")