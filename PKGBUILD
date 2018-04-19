# Script generated with Bloom
pkgdesc="ROS - rqt_bag provides a GUI plugin for displaying and replaying ROS bag files."
url='http://wiki.ros.org/rqt_bag'

pkgname='ros-melodic-rqt-bag-plugins'
pkgver='0.4.12_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin'
)

depends=('python2-cairo'
'python2-pillow'
'ros-melodic-geometry-msgs'
'ros-melodic-rosbag'
'ros-melodic-roslib'
'ros-melodic-rospy'
'ros-melodic-rqt-bag'
'ros-melodic-rqt-gui'
'ros-melodic-rqt-gui-py'
'ros-melodic-rqt-plot'
'ros-melodic-sensor-msgs'
'ros-melodic-std-msgs'
)

conflicts=()
replaces=()

_dir=rqt_bag_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_bag_plugins $srcdir/rqt_bag_plugins
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

