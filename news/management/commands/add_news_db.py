import csv
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from news.models import News


class Command(BaseCommand):
    help = "Puebla la base de datos con 5 noticias de Fake.csv"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=str(Path(settings.BASE_DIR) / "Fake.csv"),
            help="Ruta del archivo Fake.csv",
        )

    def handle(self, *args, **options):
        csv_path = Path(options["file"])

        if not csv_path.exists():
            self.stderr.write(
                self.style.ERROR(f"No se encontró el archivo: {csv_path}")
            )
            return

        with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in list(reader)[:5]:
                # Fake.csv utiliza fechas como: October 26, 2016
                news_date = datetime.strptime(
                    row["date"].strip(),
                    "%B %d, %Y",
                ).date()

                News.objects.update_or_create(
                    headline=row["title"].strip(),
                    defaults={
                        "body": row["text"].strip(),
                        "date": news_date,
                    },
                )

        self.stdout.write(
            self.style.SUCCESS("Se agregaron correctamente 5 noticias.")
        )