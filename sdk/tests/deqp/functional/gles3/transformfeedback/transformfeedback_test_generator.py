#!/usr/bin/env python

# Copyright (c) 2019 The Khronos Group Inc.
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE.txt file.

"""
  Generator for textureformat* tests.
  This file needs to be run in its folder.
"""

import sys

_DO_NOT_EDIT_WARNING = """<!--

This file is auto-generated from textureshadow_test_generator.py
DO NOT EDIT!

-->

"""

_HTML_TEMPLATE = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>WebGL Transform Feedback Tests</title>
<link rel="stylesheet" href="../../../../resources/js-test-style.css"/>
<script src="../../../../js/js-test-pre.js"></script>
<script src="../../../../js/webgl-test-utils.js"></script>
<script src="../../../../closure-library/closure/goog/base.js"></script>
<script src="../../../deqp-deps.js"></script>
<script>goog.require('functional.gles3.es3fTransformFeedbackTests');</script>
<script>goog.require('framework.opengl.gluVarTypeUtil');</script>
</head>
<body>
<div id="description"></div>
<div id="console"></div>
<canvas id="canvas" width="320" height="240"></canvas>
<script>
var wtu = WebGLTestUtils;
var gl = wtu.create3DContext('canvas', {preserveDrawingBuffer: true}, 2);

functional.gles3.es3fTransformFeedbackTests.run(gl, [%(start)s, %(end)s]);
</script>
</body>
</html>
"""

_GROUPS = [
  'position',
  'point_size',
  'basic_types_separate_points',
  'basic_types_separate_lines',
  'basic_types_separate_triangles',
  'basic_types_interleaved_points',
  'basic_types_interleaved_lines',
  'basic_types_interleaved_triangles',
  'array_separate_points',
  'array_separate_lines',
  'array_separate_triangles',
  'array_interleaved_points',
  'array_interleaved_lines',
  'array_interleaved_triangles',
  'array_element_separate_points',
  'array_element_separate_lines',
  'array_element_separate_triangles',
  'array_element_interleaved_points',
  'array_element_interleaved_lines',
  'array_element_interleaved_triangles',
  'interpolation_smooth',
  'interpolation_flat',
  'interpolation_centroid',
  'random_separate_points',
  'random_separate_lines',
  'random_separate_triangles',
  'random_interleaved_points',
  'random_interleaved_lines',
  'random_interleaved_triangles'
]

def GenerateFilename(group):
  """Generate test filename."""
  filename = group
  filename += ".html"
  return filename

def WriteTest(filename, start, end):
  """Write one test."""
  file = open(filename, "wb")
  file.write(_DO_NOT_EDIT_WARNING)
  file.write(_HTML_TEMPLATE % {
    'start': start,
    'end': end
  })
  file.close

def GenerateTests():
  """Generate all tests."""
  filelist = []
  for i in xrange(len(_GROUPS)):
    groupname = _GROUPS[i]
    filename = GenerateFilename(groupname)
    filelist.append(filename)
    WriteTest(filename, i, i+1)
  return filelist

def GenerateTestList(filelist):
  file = open("00_test_list.txt", "wb")
  file.write('\n'.join(filelist))
  file.close

def main(argv):
  """This is the main function."""
  filelist = GenerateTests()
  GenerateTestList(filelist)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
