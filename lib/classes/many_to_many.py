#!/usr/bin/env python3
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self.name = name
        self.articles = []

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("Title must be a string between 5 and 50 characters")
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article

    def articles(self):
        return self.articles

    def magazines(self):
        return list(set(article.magazine for article in self.articles))

    def topic_areas(self):
        if not self.articles:
            return None
        return list(set(article.magazine.category for article in self.articles))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise Exception("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        self.name = name
        self.category = category
        self.articles = []

    def add_article(self, author, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("Title must be a string between 5 and 50 characters")
        article = Article(author, self, title)
        self.articles.append(article)
        return article

    def articles(self):
        return self.articles

    def contributors(self):
        return list(set(article.author for article in self.articles))

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls, magazines):
        if not magazines:
            return None
        return max(magazines, key=lambda magazine: len(magazine.articles))


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("Title must be a string between 5 and 50 characters")
        self.author = author
        self.magazine = magazine
        self.title = title