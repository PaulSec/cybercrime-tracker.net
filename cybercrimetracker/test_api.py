from cybercrimetracker.cybercrimeTrackerAPI import cybercrimeTrackerAPI
import pytest

def test_answer():
	query = 'Pony'
	results = cybercrimeTrackerAPI().search(query)
	assert len(results) > 0

def test_empty_query():
	query = ''
	results = cybercrimeTrackerAPI().search(query)
	assert len(results) > 0