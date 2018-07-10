#-*- coding=UTF-8 -*-

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.starts = ""
        self.description = ""
        
    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == "movie":
            print("*****movie****")
            title = attrs["title"]
            print("title:", title)
            
    def endElement(self,tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("format:", self.format)
        elif self.CurrentData == "year":
            print("year:", self.year)
        elif self.CurrentData == "rating":
            print("rating:", self.rating)
        elif self.CurrentData == "starts":
            print("starts:", self.starts)
        elif self.CurrentData == "description":
            print("description", self.description)
        self.CurrentData = ""
        
    def characters (self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content   
        elif self.CurrentData == "year":
            self.year = content   
        elif self.CurrentData == "rating":
            self.rating = content   
        elif self.CurrentData == "starts":
            self.starts = content   
        elif self.CurrentData == "description":
            self.description = content   

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    Handler = MovieHandler()
    parser.setContentHandler( Handler ) 
    
    parser.parse("movies.xml")      
    
        
            
                
        
            