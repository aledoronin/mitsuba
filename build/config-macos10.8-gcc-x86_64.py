BUILDDIR       = '#build/release'
DISTDIR        = '#Mitsuba.app'
CXX            = 'clang++'
CC             = 'clang'
CCFLAGS        = ['-arch', 'x86_64', '-mmacosx-version-min=10.8', '-march=nocona', '-msse2', '-ftree-vectorize', '-funsafe-math-optimizations', '-fno-math-errno', '-isysroot', '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk', '-O3', '-Wall', '-g', '-pipe', '-DMTS_DEBUG', '-DSINGLE_PRECISION', '-DSPECTRUM_SAMPLES=3', '-DMTS_SSE', '-DMTS_HAS_COHERENT_RT', '-fstrict-aliasing', '-fsched-interblock', '-freorder-blocks', '-fvisibility=hidden', '-ftemplate-depth=512']
LINKFLAGS      = ['-framework', 'OpenGL', '-framework', 'Cocoa', '-arch', 'x86_64', '-mmacosx-version-min=10.8', '-Wl,-syslibroot,/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk', '-Wl,-headerpad,128']
BASEINCLUDE    = ['#include', '#dependencies/include']
BASELIBDIR     = ['#dependencies/lib']
BASELIB        = ['m', 'pthread', 'Half']
OEXRINCLUDE    = ['#dependencies/include/OpenEXR']
OEXRLIB        = ['IlmImf', 'Imath', 'Iex', 'z']
PNGLIB         = ['png']
JPEGLIB        = ['jpeg']
XERCESLIB      = ['xerces-c']
GLLIB          = ['GLEWmx', 'objc']
GLFLAGS        = ['-DGLEW_MX']
BOOSTINCLUDE   = ['#dependencies']
BOOSTLIB       = ['boost_filesystem', 'boost_system', 'boost_thread']
PYTHON26INCLUDE= ['/System/Library/Frameworks/Python.framework/Versions/2.6/Headers']
PYTHON26LIBDIR = ['/System/Library/Frameworks/Python.framework/Versions/2.6/lib']
PYTHON26LIB    = ['boost_python26', 'boost_system', 'python2.6']
PYTHON27INCLUDE= ['/System/Library/Frameworks/Python.framework/Versions/2.7/Headers']
PYTHON27LIBDIR = ['/System/Library/Frameworks/Python.framework/Versions/2.7/lib']
PYTHON27LIB    = ['boost_python27', 'boost_system', 'python2.7']
COLLADAINCLUDE = ['#dependencies/include/collada-dom', '#dependencies/include/collada-dom/1.4']
COLLADALIB     = ['collada14dom23']
QTDIR          = '#dependencies'
FFTWLIB        = ['fftw3.3']
