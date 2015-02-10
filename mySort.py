import random

# Testing myself and my python skills by writing a merge sort from memory.

def Main():
  print "Instantiating the variables..."
  sortMe = []

  print "\n****START TESTS****\n"
  left = [3,5]
  right = [1,5]
  merge(left, right)

  left = [0,0,2]
  right = [1,3,5]
  merge(left, right)

  left = []
  right = []
  merge(left, right)

  left = [1,2,3,4,5,6,7,8,9,22]
  right = [2,8,8,8,8,8,8,1000,222222]
  merge(left, right)

  left = [1]
  right = [5]
  merge(left, right)

  print "Generating random values for the array..."
  for i in range(0, 20):
    sortMe.append(random.randint(1, 200))

  print "Finished populating the array..."

  print "\n\n\n****STARTING RECURSIVE SORT TEST*****"
  print "List to sort: " + str(sortMe)
  print "FINAL RESULT!!!\n" + str(recursive_merge(sortMe))

def iterative_merge(sortMe):
  # Returns a sorted array using an iterative merge sort

  # Args:
  #   sortMe: the array that needs to be sorted
  # Returns:
  #   okSorted: the sorted array

  print "Entering iterative merge sort"

def recursive_merge(sortMe):
  # Returns a sorted array using an iterative merge sort

  # Args:
  #   toBeSorted: the array that needs to be sorted
  # Returns:
  #   okSorted: the sorted array

  print "Entering recursive merge sort"

  if (len(sortMe) <= 0):
    print "recursion has hit base case |0|"
    return []
  elif (len(sortMe) == 1):
    print "recursion has hit base case |1|"
    return sortMe
  else: 
    half = len(sortMe) / 2
    print "recursion has not hit a base case, half = " + str(half)
    print "L  recursing on " + str(sortMe[:half])
    left = recursive_merge(sortMe[:half])
    print "R  recursing on " + str(sortMe[half:])
    right = recursive_merge(sortMe[half:])
    #  Note: this will guarentee left and right are at least > 1
    print "merging " + str(left) + " with " + str(right)
    return merge(left, right)

def merge(left, right):
  # merges two array together and returns the merged array

  # Args:
  #   left: Sorted first half to be merged. Size > 0
  #   right: Sorted second half to be merged. Size > 0
  # Returns:
  #   okMerged: the merged array

  okMerged = []
  if (len(left) == 0 or len(right) == 0):
    print "    First base case!"
    print "    Merged! " + str(left + right)
    return left + right
  else:
    l = 0
    r = 0

    retListLen = len(left) + len(right)

    for i in range(0, retListLen):

      if (l < len(left) and r < len(right)):
        if (left[l] < right[r]):
          okMerged.append(left[l])
          i += 1
          l += 1
        else: 
          okMerged.append(right[r])
          i += 1
          r += 1
      elif (l >= len(left)):
        print "    Merged! " + str(okMerged + right[r:])
        return okMerged + right[r:]
      elif (r >= len(right)):
        print "    Merged! " + str(okMerged + left[l:])
        return okMerged + left[l:]

    print "    Merged! " + str(okMerged)
    return okMerged

if __name__ == '__main__':
  Main()



















