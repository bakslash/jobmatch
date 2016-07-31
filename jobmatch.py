#!/usr/bin/env python
"""
Given 50 randomly located drivers, map them to some random
number of randomly located jobs such that
total distance to jobs is minimised"""
from random import sample, random
from collections import defaultdict

driver_jobs = defaultdict(list)
pool_of_nums = range(1, 100)
SAMPLE_SIZE = 50
randomly_selected_drivers = sample(pool_of_nums, SAMPLE_SIZE)

for driver in randomly_selected_drivers:s
    # select random maximum jobs to be assigned to driver
    # add one to make sure driver has at least one job
    num_of_jobs = int(random() * 50) + 1

    # select random jobs whose sum == num_of_jobs
    selected_jobs = sample(pool_of_nums, num_of_jobs)

    # assign the jobs to the driver
    # sort the selected jobs because we assume the difference between
    # the driver number and the job number is the distance between the two
    # and so keeping the jobs in ascending order ensures the driver covers
    # the least distance while going to all the jobs
    driver_jobs[driver].extend(sorted(selected_jobs))

    print('Driver {} -- Jobs {}'.format(driver, driver_jobs[driver]))

