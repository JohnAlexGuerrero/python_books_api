from datetime import datetime
from typing import List

class Author(object):
    '''
    Author object that is composed of the
    
    :parma id
    :param name
    :param gender
    :param born
    :param born_place
    :param rating_average
    :param rating_count
    :param review_count
    
    '''
    id: int
    name: str
    gender: str
    born: str
    born_place: int
    rating_average: float
    rating_count: int
    review_count: int
    
    def __init__(self,id: int, name: str, gender: str, born: str, born_place: int, rating_average: float):
      self.name = name
      self.id = id
      self.gender = gender
      self.born = born
      self.rating_average = rating_average
      self.born_place = born_place
     

class Book(object):
    '''
        Book object that is composed of the 
        
        :param id
        :param name
        :param num_pages
        :param rating_average
        :param published
        :param editorial
        :param reviews_counts
        :param lenguage:
        :param author
        :param isbn
    '''
    id: int
    name : str
    num_pages : int
    rating_average : float
    published : str
    editorial : int
    reviews_counts : int
    language : int
    authors : List
    isbn : str

    def __init__(self, id:int, name:str, num_pages:int, rating_average:float, published: str, editorial: int, reviews_counts: int, language: int, authors: List, isbn: str):
        self.id = id
        self.name = name
        self.num_pages = num_pages
        self.rating_average = rating_average
        self.published = published
        self.editorial = editorial
        self.reviews_counts = reviews_counts
        self.language = language
        self.authors = List[Author] | authors
        self.isbn = isbn
    
    def add_author(self, author: Author):
        self.authors.append(author)
    

class Editorial(object):
    '''
    Editorial object that is composed of the 
    
    :param id
    :paran name
    
    Also, Editorial has a list of books 
    :field books: Editorial books list
    '''
    
    id: int
    name: str
    
    def __init__(self, id: int, name: str):
      self.name = name
      self.id = id
      self.books: List[Book] = []
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def books_count(self)->int:
        return len(self.books)


class Country(object):
    '''
    Country object that composed of the
    
    :param id
    :param name
    :param latitud
    :param longitud
    '''
    
    id: int
    name: str
    latitud: str
    longitud: str
    
    def __init__(self, id: int, name: str, latitud: str, longitud: str):
      self.name = name
      self.id = id
      self.latitud = latitud
      self.longitud = longitud
      self.authors = List[Author] = []
      
    def add_author(self, author: Author):
        self.authors.append(author)
    
    def authors_count(self)->int:
        return len(self.authors)
