from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Author


class AutorModelSerializer(HyperlinkedModelSerializer):
      class Meta:
          model = Author
          fields = '__all__'
