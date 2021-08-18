import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment

def add_command(name,cl,id):


   # root = tree.getroot()
   # top = Element('top')
   # child = SubElement(top, 'child')
    #child.text = 'This child contains text.'
    #child_with_tail = SubElement(top, 'child_with_tail')
    #child_with_tail.text = 'This child has regular text.'
    #child_with_tail.tail = 'And "tail" text.'



    tree = ET.parse('command.xml')
    root = tree.getroot()
    newNode = ET.Element("Command")
    newNodeName=ET.Element('id')
    newNodeName.text = str(id)
    newNode.append(newNodeName)
    newNodeName=ET.Element('name')

    newNodeName.text = str(name)
    newNode.append(newNodeName)
    newNodeName=ET.Element('content')
    newNodeName.text = str(cl)
    newNode.append(newNodeName)
    root.insert(0, newNode)
    #file_handle = open("command.xml.xml","wb")
    tree.write('command.xml')
    #file_handle.close()
    #ET.dump(newNodeName)
    return
def delete_command(name):
    tree = ET.parse('command.xml')
    root = tree.getroot()
    for country in root.findall('Command'):
        rank = (country.find('name').text)

        if rank ==str(name):

                root.remove(country)

    tree.write('command.xml')
    return
def delete_commandid(id):
    tree = ET.parse('command.xml')
    root = tree.getroot()
    for country in root.findall('Command'):
        rank = (country.find('id').text)

        if rank ==str(id):

                root.remove(country)

    tree.write('command.xml')
    return

def update_command(xmlfile,namee):
    tree = ET.parse(str(xmlfile))
    root = tree.getroot()
    for country in root.findall('Command'):
        rank = (country.find('name').text)

        if rank ==str(namee):
            idd=(country.find('id').text)
            name=(country.find('name').text)
            script=(country.find('content').text)
    return idd,name,script
#delete_commandid("100")
#print(update_command("command.xml","lister")[0])

#add_command("aaa","zaa","16")
