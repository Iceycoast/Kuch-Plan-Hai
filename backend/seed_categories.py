from sqlalchemy.orm import Session
from app.db import get_db
from app.models.category import Category

def seed_categories():
    
    try:
        db = next(get_db())

        categories = [
            {"name": "Food", "slug": "food", "sort_order": 1},
            {"name": "Entertainment", "slug": "entertainment", "sort_order": 2},
            {"name": "Activities", "slug": "activities", "sort_order": 3},
            {"name": "Casual Hangouts", "slug": "casual-hangouts", "sort_order": 4}
        ]

        for cat_data in categories:
            existing = db.query(Category).filter(Category.slug == cat_data["slug"]).first()
            if not existing:
                category = Category(**cat_data)
                db.add(category)

        db.commit()
        print("Categories seeded successfully!")

    except Exception as e:
        print(f"Error seeding categories: {e}")
        db.rollback()


if __name__ == "__main__":
    seed_categories()