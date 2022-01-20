from django.db import models
import datetime
import os

def filepath(request, filename):
	old_filename = filename
	timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
	filename = "%s%s" % (timeNow, old_filename)
	return os.path.join('uploads/', filename)

class Item(models.Model):
	name = models.TextField(max_length=191)
	price = models.TextField(max_length=50)
	date = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to=filepath, null=True, blank=True)
		
	@property
	def is_past_due(self):
		if datetime.date.today() > self.date:
			yesterday=datetime.date.today() - datetime.timedelta(days=1)
			if yesterday > self.date:
				return True
		return True

