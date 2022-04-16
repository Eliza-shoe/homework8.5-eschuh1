import unittest
from unittest.mock import patch, MagicMock

# from database import undo_last_review

global mock_ratings
mock_ratings = {
    1: {"rating": 5, "name": "Eliza", "timestamp": 1246},
    2: {"rating": 4, "name": "Nur", "timestamp": 1812},
    3: {"rating": 3, "name": "Alina", "timestamp": 120},
    4: {"rating": 2, "name": "Anish", "timestamp": 2145},
    5: {"rating": 1, "name": "John", "timestamp": 2359},
}


class DB_Tests(unittest.TestCase):
    """def test_null(self):
    self.assertEqual(undo_last_review(), 0)"""

    def test_query(self):
        with patch("undo_last_review.Rating.query.all") as mock_rating:
            mock_rating.return_value = mock_ratings[1]
            return mock_rating.return_value

    def test_delete(self):
        with patch("undo_last_review.db.session.delete"):
            most_recent = mock_ratings[1]
            mock_ratings.remove(most_recent)
            return None

    def test_commit(self):
        with patch("undo_last_review.db.session.commit"):
            return None


if __name__ == "__main__":
    unittest.main()


"""def undo_last_review():

    Pops out the most recent review and deletes it from the DB. Returns the review object that was just removed.
 

    user_ratings = Rating.query.all()
    most_recent = max(
        user_ratings, key=lambda x: x.timestamp
    )  # concise Python way of finding the element with the largest timestamp attribute in a list
    db.session.delete(most_recent)
    db.session.commit()
    return most_recent
"""
