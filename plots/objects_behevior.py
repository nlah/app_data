"""
"A universal convention supplies all of maintainability,
clarity, consistency, and a foundation for good programming habits too.
What it doesn't do is insist that you follow it against your will. That's Python!"
—Tim Peters on comp.lang.python, 2001-06-16
"""
import io
import pandas as pd
from . upc import UpcWalmart
from . models import WalmartModel, UserProfile
from django.forms.models import model_to_dict


class User(object):
    """
       Object to interact user and db
    """

    url = 'http://api.walmartlabs.com/v1/items'

    def __init__(self, user='test'):
        self.user = user
        try:
            key = UserProfile.objects.get(user=self.user).key
            self.user_upc = UpcWalmart(key)
        except Exception as err:
            self.user_upc = err.args

    def set_key(self, key: str):
        if UpcWalmart.check_key(key):
            print(UserProfile.objects.filter(user=self.user))
            if len(UserProfile.objects.filter(user=self.user)) > 0:
                UserProfile.objects.filter(user=self.user).update(key=key)
            else:
                UserProfile(user=self.user, key=key).save()
            self.user_upc = UpcWalmart(key)
            return 1
        else:
            return -1

    def key_walmart(self):
        """ Return key Walmart if exist """

        if isinstance(self.user_upc, UpcWalmart):
            return self.user_upc.key
        else:
            return "key Error"

    def set_upc(self, upc):
        """
        Args:
          upc:
        Returns:
            -1  if not add in db
             1 if add in db
             self.user_upc if  self.user_upc not UpcWalmart object
        """

        if isinstance(self.user_upc, UpcWalmart):
            try:
                WalmartModel.objects.get(upc=upc)
                return -1
            except WalmartModel.DoesNotExist:
                data = self.user_upc.get(upc)
                try:
                    WalmartModel(**data).save()
                except TypeError:
                    return -1
            return 1
        else:
            return self.user_upc

    def get_upc(self):
        """ """
        return [model_to_dict(i) for i in WalmartModel.objects.all()]

    def get_upc_limit_sort(self, start, end, key, sort_type):
        """
        Args:
          start:
          end:
          key:
          sort_type:
        Returns:

        """

        key = (key, '-' + key)[sort_type == 1]
        return [model_to_dict(i) for i in WalmartModel.objects.all().order_by(str(key))[start:start + end]]

    def get_csv(self):
        """ Return csv file """

        csv_data = []
        column_name = self.user_upc.get_header_upc()
        for i in column_name:
            csv_data.append([])
        for i in self.get_upc():
            for j in range(len(column_name)):
                try:
                    csv_data[j].append(i[column_name[j]])
                except:
                    csv_data[j].append(-1)
        df = pd.DataFrame(csv_data).transpose()
        df.columns = column_name
        return df.to_csv(index=False)

    def set_csv(self, file_data):
        """
        Add upc from csv in db
        Args:
          file_data:
        Returns:
            list of not added keys
        """

        try:
            df = pd.read_csv(io.StringIO(file_data.decode('utf-8')), dtype={'upc': str})['upc']
        except KeyError:
            return -1
        out = []
        for i in df:
            if self.set_upc(i) == -1:
                out.append(i)
        print(out)
        return out

    def del_upc(self, upc: str):
        return WalmartModel.objects.filter(upc=upc).delete()

    def count_upc(self):
        """ Coutn upc in db """

        return WalmartModel.objects.count()
