from django.db import models

# Education.
class Education(models.Model):
    period = models.CharField(max_length=9, verbose_name="Period")
    title = models.CharField(max_length=100, verbose_name="Title/Grade")
    school = models.CharField(max_length=100, verbose_name="School")
    description = models.TextField(verbose_name="Description")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")

    # Metadata
    class Meta:
        # Order by field 'created'.
        # '-' means inverse order (show new first).
        ordering = ["-created"]
    
    # Return the title of the current project.
    def __str__(self):
        return self.title

# Experience.
class Experience(models.Model):
    period = models.CharField(max_length=9, verbose_name="Period")
    title = models.CharField(max_length=100, verbose_name="Title/Job")
    enterprise = models.CharField(max_length=100, verbose_name="Enterprise")
    description = models.TextField(verbose_name="Description")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")

    # Metadata
    class Meta:
        # Order by field 'created'.
        # '-' means inverse order (show new first).
        ordering = ["-created"]
    
    # Return the title of the current project.
    def __str__(self):
        return self.title

# Awards.
class Awards(models.Model):
    period = models.CharField(max_length=9, verbose_name="Period")
    title = models.CharField(max_length=100, verbose_name="Title/Award")
    enterprise = models.CharField(max_length=100, verbose_name="Enterprise")
    description = models.TextField(verbose_name="Description")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")

    # Metadata
    class Meta:
        # Order by field 'created'.
        # '-' means inverse order (show new first).
        ordering = ["-created"]
    
    # Return the title of the current project.
    def __str__(self):
        return self.title