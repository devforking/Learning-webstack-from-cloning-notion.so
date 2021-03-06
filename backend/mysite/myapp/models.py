# this is a recursive model
from django.db import models


class elements(models.Model):
    tag = models.CharField(blank=True, null=True, max_length=20)
    text = models.TextField(blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    # problem: styles replace spaces with slashes (/)
    # I tried: json field but did'nt work.
    style = models.JSONField(blank=True, null=True)
    table = models.JSONField(blank=True, null=True)
    main = models.ForeignKey(
        'self', null=True, blank=True, related_name="sub", on_delete=models.PROTECT)

    def __str__(self):
        return "<elements: {} {}>".format(self.tag, self.text, self.src, self.style, self.table)

    def __repr__(self):
        return self.__str__()


class styles(models.Model):
    name = models.TextField(blank=True, null=True, max_length=50)
    style = models.JSONField(blank=True, null=True)
    main = models.ForeignKey(
        'self', null=True, blank=True, related_name="sub", on_delete=models.PROTECT)


class components(models.Model):
    name = models.TextField(blank=True, null=True, max_length=50)
    tag = models.CharField(blank=True, null=True, max_length=20)
    text = models.TextField(blank=True, null=False)
    src = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)

    main = models.ForeignKey(
        'self', null=True, blank=True, related_name="sub", on_delete=models.PROTECT)
