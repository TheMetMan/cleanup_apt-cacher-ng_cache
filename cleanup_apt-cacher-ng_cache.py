#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
"""
2025-08-01
Version 0.0.1
Script to clean the apt-cacher-ng tmp files folder
An Idea I got from here https://forums.gentoo.org/viewtopic-p-8770951.html

"""
import os
import subprocess

def get_space_used(_path):
    """
    method to get the space used in the path
    :param _path: Path to files as a string
    :return: space in Gb
    """
    command = 'du -sh {}'.format(_path)
    result = subprocess.check_output(command, shell=True, text=True)
    result = result.split('\t')
    if len(result[0]) > 1:
        result = result[0][:-1]
    return float(result[0])

def get_files(_path):
    """
    method to get the files in the path
    :param _path: Path to files as a string
    :return: List of the files in the path and the number of files
    """
    list = []
    list_full = []
    count = 0
    for (root, dirs, file) in os.walk(_path):
        for f in file:
            count += 1
            list.append(f)
            list_full.append(os.path.join(root, f))
    return list, list_full, count

if __name__ == '__main__':
    """
    Main
    """
    print('Cleaning up the Apt Cacher NG Cache to save bloat!')
    # Gentoo Distfiles
    path = '/var/cache/distfiles/'
    distfiles_space = get_space_used(path)
    distfiles_list, distfiles_full_list, distfiles_count = get_files(path)
    # print('Total Files in Cache = {}'.format(distfiles_count))
    #
    # Apt Cache NG Cached Files
    path = '/var/tmp/gentoo/distfiles/'
    cachefiles_space = get_space_used(path)
    cachefiles_list, cachefiles_full_list, cachefiles_count = get_files(path)
    #
    remove_count = 0
    for f in cachefiles_full_list:
        fname = os.path.basename(f)
        if fname not in distfiles_list:
            if os.path.exists(f):
                # print('Removing File {}'.format(f))
                remove_count += 1
                os.remove(f)
    print('Total DistFiles = {} and CacheFiles = {} - Removing {} Files'.format(distfiles_count, cachefiles_count, remove_count))
    saved_space = cachefiles_space - distfiles_space
    print('Distfiles take up {}G space and the Cache Files took up {}G space. So we have saved {}G of Disk Space'.format(distfiles_space, cachefiles_space, saved_space))
