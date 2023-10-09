from rest_framework import serializers
import Topping # noqa

'''
Like @DanEEStart said, DjangoRestFramework don't have a simple way to extend the 'all' value for fields, 
because the get_field_names methods seems to be designed to work that way.
=> https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/serializers.py#L1019

But fortunately you can override this method to allow a simple way to include all fields and relations 
without enumerate a tons of fields.

I override this method like this:
'''


class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = '__all__'
        extra_fields = ['pizzas']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(ToppingSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
        

# http://stackoverflow.com/questions/14573102/how-do-i-include-related-model-fields-using-django-rest-framework


'''
Note that this method only change the behaviour of this serializer, and the extra_fields attribute only 
works on this serializer class.

If you have a tons of serializer like this, you can create a intermediate class to include 
this get_fields_names method in one place and reuse'em many times. Some like this:
'''

class CustomSerializer(serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class ToppingSerializer(CustomSerializer):

    class Meta:
        model = Topping
        fields = '__all__'
        extra_fields = ['pizzas']

class AnotherSerializer(CustomSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        extra_fields = ['comments']






# 2

'''
I just checked the source code of Django Rest Framework. The behaviour you want seems not to be supported in the Framework.

The fields option must be a list, a tuple or the text __all__.

Here is a snippet of the relevant source code:
'''

'''
ALL_FIELDS = '__all__'
if fields and fields != ALL_FIELDS and not isinstance(fields, (list, tuple)):
    raise TypeError(
        'The `fields` option must be a list or tuple or "__all__". '
        'Got %s.' % type(fields).__name__
    )
    
You cannot add 'all' additionally to the tuple or list with fields...


man, this is such a basic feature, every time I look into django it looks like everything is broken or 
set on stone, no way to make smart factories or anything, just write a ton of useless code 
for any simple thing you want to do. thanks for the answer
'''

# 3

'''
The fields="__all__" option can work by specifying an additional field manually as per the following examples. 
This is by far the cleanest solution around for this issue.

Nested Relationships

http://www.django-rest-framework.org/api-guide/relations/#nested-relationships

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'
I would assume this would work for any of the other related field options listed on the same page
: http://www.django-rest-framework.org/api-guide/relations/#serializer-relations

Reverse relation example

class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(source='album_id')

    class Meta:
        model = Track
        fields = '__all__'
Note: Created using Django Rest Framework version 3.6.2, subject to change. Please add a comment if any 
future changes break any examples posted above.
'''


# 4

'''
Hi I could achieve the expected result by using Django's _meta API , which seems to be available since Django 1.11. 
So in my serializer I did:

=> https://docs.djangoproject.com/en/2.0/ref/models/meta/

model = MyModel
fields = [field.name for field in model._meta.fields]
fields.append('any_other_field')
In programming there's always many ways to achieve the same result, but this one above, has really worked for me.

Cheers!


This won't work if you declare extra fields in your serializer, that are not in the model. 
E.g. if you need to send extra data at the point of serialization. Therefore, it shouldn't be accepted as 
a generally working solution. – 

'''


# 4

'''
If you are trying to basically just add extra piece of information into the serialized object, you don't need to change the fields part at all. To add a field you do:

class MySerializer(serializers.ModelSerializer):
   ...
   new_field = serializers.SerializerMethodField('new_field_method')

   def new_field_method(self, modelPointer_):
      return "MY VALUE"
Then you can still use

class Meta:
   fields = '__all__'

   => This should be the accepted answer. thanks ! – 

'''


# 5

'''
This is how i did it, much more easier

class OperativeForm(forms.ModelForm):
    class Meta:
        model = Operative
        fields = '__all__'
        exclude = ('name','objective',)
        widgets = {'__all__':'required'}

'''


# 6

'''
Building on top of @Wand's wonderful answer:

def build_fields(mdl,extra=[],exclude=[]):
    fields = [field.name for field in mdl._meta.fields if field.name not in exclude]
    fields += extra
    return fields
Usage:

model = User
fields = build_fields(model, ['snippets'], ['password'])
Will return all fields from the User model, with the related field snippets, without the password field.


'''