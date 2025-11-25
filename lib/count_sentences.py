#!/usr/bin/env python3
class MyString:
    
    def __init__(self, value=''):
        """Initialize MyString with a value property."""
        self.value = value
    
    def get_value(self):
        """Retrieve the string value."""
        return self._value
    
    def set_value(self, value):
        """Set the string value with validation."""
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    # Create value property
    value = property(get_value, set_value)
    
    def is_sentence(self):
        """
        Check if the value ends with a period.
        
        Returns:
            bool: True if value ends with '.', False otherwise
        """
        return self.value.endswith('.')
    
    def is_question(self):
        """
        Check if the value ends with a question mark.
        
        Returns:
            bool: True if value ends with '?', False otherwise
        """
        return self.value.endswith('?')
    
    def is_exclamation(self):
        """
        Check if the value ends with an exclamation mark.
        
        Returns:
            bool: True if value ends with '!', False otherwise
        """
        return self.value.endswith('!')
    
    def count_sentences(self):
        """
        Count the number of sentences in the value.
        A sentence ends with '.', '!', or '?'
        
        Returns:
            int: Number of sentences
        """
        # Handle empty string
        if not self.value:
            return 0
        
        # Replace multiple punctuation marks with single ones
        # This handles cases like "!!" or "..." or "?!"
        text = self.value
        
        # Replace all sentence-ending punctuation with a common delimiter
        # First, replace multiple punctuation with single
        while '!!' in text or '??' in text or '..' in text:
            text = text.replace('!!', '!')
            text = text.replace('??', '?')
            text = text.replace('..', '.')
        
        # Replace all sentence endings with a common marker
        text = text.replace('!', '.')
        text = text.replace('?', '.')
        
        # Split on periods
        sentences = text.split('.')
        
        # Filter out empty strings and whitespace-only strings
        sentences = [s for s in sentences if s.strip()]
        
        return len(sentences)


