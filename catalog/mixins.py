from uuslug import uuslug


class SaveModelSlugMixin:

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(s=self.title, instance=self)
        return super().save(*args, **kwargs)
