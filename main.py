import sys
import unittest
from unittest import TestResult

from dex.rs.pokemon_list import PokemonListResource


class SmogonDataProvider(object):
    @staticmethod
    def run_tests() -> TestResult:
        testSuite = unittest.TestLoader().discover('.', pattern='*.py')
        testResult = TestResult()
        return testSuite.run(testResult)


if __name__ == "__main__":
    #testResult = SmogonDataProvider.run_tests()
    #if testResult.errors:
    #    for testCase, errorMessage in testResult.errors:
    #        print(testCase.id(), errorMessage)
    #    sys.exit(1)

    print(len(PokemonListResource.getListElements()))
