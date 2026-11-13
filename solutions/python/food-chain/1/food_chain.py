def build_verse(animal_n):

    animals = {1: ['fly', ''],
        2: ['spider', 'It wriggled and jiggled and tickled inside her.'],
        3: ['bird', 'How absurd to swallow a bird!'],
        4: ['cat', 'Imagine that, to swallow a cat!'],
        5: ['dog', 'What a hog, to swallow a dog!'],
        6: ['goat', 'Just opened her throat and swallowed a goat!'],
        7: ['cow', "I don't know how she swallowed a cow!"],
        8: ['horse', "She's dead, of course!"]
        }

    poem = ""
    joker = "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
    prefix = "I know an old lady who swallowed a "
    first_verse = prefix + animals[animal_n][0] + '.'
    second_verse = animals[animal_n][-1]
    catch_verse_1 = "She swallowed the "
    catch_verse_2 = " to catch the "
    

    if animal_n > 1:
        catch_verse = catch_verse_1 + animals[animal_n][0] + catch_verse_2 + animals[animal_n-1][0] + '.'
    if animal_n == 3:
        poem = first_verse + '\n' + second_verse + '\n' + joker
    elif animal_n != 1:
        poem = first_verse + '\n' + second_verse + '\n' + catch_verse
    else:
        poem = first_verse

    return poem

def build_poem(verse_number):
    if verse_number == 8:
        return build_verse(8).splitlines()[:-1]
    else:
        catch_verses = []
        for i in range(2,verse_number+1):
            catch_verses.append(build_verse(i).splitlines()[-1])

        first_verses = build_verse(verse_number).splitlines()[:2]
        poem = first_verses + catch_verses[::-1]
        final_poem = (first_verses + catch_verses[::-1] + ["I don't know why she swallowed the fly. Perhaps she'll die."])
        return final_poem

def recite(start_verse, end_verse):
    poem = []

    for i in range(start_verse, end_verse+1):
       poem += build_poem(i)
       poem += ['']
    
    return poem[:-1]
    