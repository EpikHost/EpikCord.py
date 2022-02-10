from typing import (Optional)


class Embed: # Always wanted to make this class :D
    def __init__(self,*, title: Optional[str], description: Optional[str], color:Optional[Colour], colour:Optional[Colour], url:Optional[str]):
        
        self.title: Optional[str] = title
        self.type: Optional[str] = type
        self.description: Optional[str] = description
        self.url: Optional[str] = url
        self.timestamp: Optional[str] = None
        self.color: Optional[Colour] = color or colour
        self.footer: Optional[str] = None
        self.image: Optional[str] = None
        self.thumbnail: Optional[str] = None
        self.valid_styles: Optional[str] = None
        self.provider: Optional[str] = None
        self.author: Optional[EmbedAuthor] = None
        self.fields: Optional[List[str]] = None
        
    def add_field(self,*, name: str, value: str, inline: bool = False):
        self.fields.append({"name": name, "value": value, "inline": inline})
        
    def set_thumbnail(self, url: str):
        self.thumbnail = url
    
    def set_image(self, url:str):
        self.image = url
    
    def set_footer(self, footertxt:str):
        self.footer = footertxt

    def set_author(self, author:EmbedAuthor):
        self.author = author

    def set_timestamp(self, timestamp):
        pass #someone do this??

    @property
    def fields(self):
        return self.fields #needs improvement