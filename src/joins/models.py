from django.db import models

# Create your models here.

class Join(models.Model):
	email = models.EmailField()
	friend = models.ForeignKey("self", related_name='referral', null=True, blank=True)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s" %(self.email)

	class Meta:
		unique_together = ("email", "ref_id",)

# class JoinFriends(models.Model):
# 	email = models.OneToOneField(Join, related_name = "Sharer")
# 	friends = models.ManyToManyField(Join, related_name="Friend", \
# 											null=True, blank=True)
# 	emailall = models.ForeignKey(Join, related_name='emailall')

# 	def __unicode__(self):
# 		print "friends are ", self.friends.all()
# 		print self.emailall
# 		print self.email
# 		return self.email.email





# In case extra fields are added, database error is handled by south and migration
# Step 1) Install south: pip install south, add south to settings.py in INSTALLED APPS
# Step 2) Ensure Model is in the synced database
# Step 3) Convert the model to south with: python manage.py convert_to_south appname
# Step 4) Make changes to model (eg add new fields: ip_address = models.Charfields())
# Step 5) Run schemamigration: python manage.py schemamigration appname --auto
# Step 6) Run migrate: python manage.py migrate

# south is inside Django 1.7