# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.87
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PartStudiosGetSketchInfoResponse200GeomEntities(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'knots': 'list[float]',
        'end_point': 'list[float]',
        'point': 'list[float]',
        'mid_point': 'list[float]',
        'entity_type': 'str',
        'start_vector': 'list[float]',
        'radius': 'float',
        'clockwise': 'bool',
        'start_point': 'list[float]',
        'end_param': 'float',
        'start_param': 'float',
        'end_point_ids': 'list[str]',
        'end_derivative': 'list[float]',
        'start_derivative': 'list[float]',
        'minor_radius': 'float',
        'rational': 'bool',
        'curve_length': 'float',
        'control_points': 'list[object]',
        'direction': 'list[float]',
        'degree': 'float',
        'end_handle': 'list[float]',
        'quarter_point': 'list[float]',
        'interpolation_points': 'list[float]',
        'major_radius': 'float',
        'end_vector': 'list[float]',
        'center': 'list[float]',
        'number_control_points': 'float',
        'start_handle': 'list[float]',
        'periodic': 'bool',
        'is_construction': 'bool'
    }

    attribute_map = {
        'knots': 'knots',
        'end_point': 'endPoint',
        'point': 'point',
        'mid_point': 'midPoint',
        'entity_type': 'entityType',
        'start_vector': 'startVector',
        'radius': 'radius',
        'clockwise': 'clockwise',
        'start_point': 'startPoint',
        'end_param': 'endParam',
        'start_param': 'startParam',
        'end_point_ids': 'endPointIds',
        'end_derivative': 'endDerivative',
        'start_derivative': 'startDerivative',
        'minor_radius': 'minorRadius',
        'rational': 'rational',
        'curve_length': 'curveLength',
        'control_points': 'controlPoints',
        'direction': 'direction',
        'degree': 'degree',
        'end_handle': 'endHandle',
        'quarter_point': 'quarterPoint',
        'interpolation_points': 'interpolationPoints',
        'major_radius': 'majorRadius',
        'end_vector': 'endVector',
        'center': 'center',
        'number_control_points': 'numberControlPoints',
        'start_handle': 'startHandle',
        'periodic': 'periodic',
        'is_construction': 'isConstruction'
    }

    def __init__(self, knots=None, end_point=None, point=None, mid_point=None, entity_type=None, start_vector=None, radius=None, clockwise=None, start_point=None, end_param=None, start_param=None, end_point_ids=None, end_derivative=None, start_derivative=None, minor_radius=None, rational=None, curve_length=None, control_points=None, direction=None, degree=None, end_handle=None, quarter_point=None, interpolation_points=None, major_radius=None, end_vector=None, center=None, number_control_points=None, start_handle=None, periodic=None, is_construction=None):  # noqa: E501
        """PartStudiosGetSketchInfoResponse200GeomEntities - a model defined in Swagger"""  # noqa: E501

        self._knots = None
        self._end_point = None
        self._point = None
        self._mid_point = None
        self._entity_type = None
        self._start_vector = None
        self._radius = None
        self._clockwise = None
        self._start_point = None
        self._end_param = None
        self._start_param = None
        self._end_point_ids = None
        self._end_derivative = None
        self._start_derivative = None
        self._minor_radius = None
        self._rational = None
        self._curve_length = None
        self._control_points = None
        self._direction = None
        self._degree = None
        self._end_handle = None
        self._quarter_point = None
        self._interpolation_points = None
        self._major_radius = None
        self._end_vector = None
        self._center = None
        self._number_control_points = None
        self._start_handle = None
        self._periodic = None
        self._is_construction = None
        self.discriminator = None

        if knots is not None:
            self.knots = knots
        if end_point is not None:
            self.end_point = end_point
        if point is not None:
            self.point = point
        if mid_point is not None:
            self.mid_point = mid_point
        if entity_type is not None:
            self.entity_type = entity_type
        if start_vector is not None:
            self.start_vector = start_vector
        if radius is not None:
            self.radius = radius
        if clockwise is not None:
            self.clockwise = clockwise
        if start_point is not None:
            self.start_point = start_point
        if end_param is not None:
            self.end_param = end_param
        if start_param is not None:
            self.start_param = start_param
        if end_point_ids is not None:
            self.end_point_ids = end_point_ids
        if end_derivative is not None:
            self.end_derivative = end_derivative
        if start_derivative is not None:
            self.start_derivative = start_derivative
        if minor_radius is not None:
            self.minor_radius = minor_radius
        if rational is not None:
            self.rational = rational
        if curve_length is not None:
            self.curve_length = curve_length
        if control_points is not None:
            self.control_points = control_points
        if direction is not None:
            self.direction = direction
        if degree is not None:
            self.degree = degree
        if end_handle is not None:
            self.end_handle = end_handle
        if quarter_point is not None:
            self.quarter_point = quarter_point
        if interpolation_points is not None:
            self.interpolation_points = interpolation_points
        if major_radius is not None:
            self.major_radius = major_radius
        if end_vector is not None:
            self.end_vector = end_vector
        if center is not None:
            self.center = center
        if number_control_points is not None:
            self.number_control_points = number_control_points
        if start_handle is not None:
            self.start_handle = start_handle
        if periodic is not None:
            self.periodic = periodic
        if is_construction is not None:
            self.is_construction = is_construction

    @property
    def knots(self):
        """Gets the knots of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (spline[Segment]) The spline knot vector  # noqa: E501

        :return: The knots of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._knots

    @knots.setter
    def knots(self, knots):
        """Sets the knots of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (spline[Segment]) The spline knot vector  # noqa: E501

        :param knots: The knots of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._knots = knots

    @property
    def end_point(self):
        """Gets the end_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (lineSegment, arc, ellipticArc, curvePoints=true) The end point of the segment  # noqa: E501

        :return: The end_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (lineSegment, arc, ellipticArc, curvePoints=true) The end point of the segment  # noqa: E501

        :param end_point: The end_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._end_point = end_point

    @property
    def point(self):
        """Gets the point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (line) An arbitrary point on the line  # noqa: E501

        :return: The point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (line) An arbitrary point on the line  # noqa: E501

        :param point: The point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._point = point

    @property
    def mid_point(self):
        """Gets the mid_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (curvePoints=true) The point that is half    way between the start and end of the curve  # noqa: E501

        :return: The mid_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._mid_point

    @mid_point.setter
    def mid_point(self, mid_point):
        """Sets the mid_point of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (curvePoints=true) The point that is half    way between the start and end of the curve  # noqa: E501

        :param mid_point: The mid_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._mid_point = mid_point

    @property
    def entity_type(self):
        """Gets the entity_type of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        The type of the entity. Can be one of:    \"point\", \"line\", \"lineSegment\", \"circle\", \"arc\", \"ellipse\", \"ellipticArc\", \"spline\", \"splineSegment\",    \"interpolatedSpline\", \"interpolatedSplineSegment\", \"unknownGeometry\".  # noqa: E501

        :return: The entity_type of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this PartStudiosGetSketchInfoResponse200GeomEntities.

        The type of the entity. Can be one of:    \"point\", \"line\", \"lineSegment\", \"circle\", \"arc\", \"ellipse\", \"ellipticArc\", \"spline\", \"splineSegment\",    \"interpolatedSpline\", \"interpolatedSplineSegment\", \"unknownGeometry\".  # noqa: E501

        :param entity_type: The entity_type of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def start_vector(self):
        """Gets the start_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (curvePoints=true) The tangent vector    at the start of the curve  # noqa: E501

        :return: The start_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._start_vector

    @start_vector.setter
    def start_vector(self, start_vector):
        """Sets the start_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (curvePoints=true) The tangent vector    at the start of the curve  # noqa: E501

        :param start_vector: The start_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._start_vector = start_vector

    @property
    def radius(self):
        """Gets the radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (circle, arc). The circular radius  # noqa: E501

        :return: The radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (circle, arc). The circular radius  # noqa: E501

        :param radius: The radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._radius = radius

    @property
    def clockwise(self):
        """Gets the clockwise of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (arc, ellipticArc) If true, the segment    is oriented clockwise from the startPoint to the endPoint around the center.  # noqa: E501

        :return: The clockwise of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: bool
        """
        return self._clockwise

    @clockwise.setter
    def clockwise(self, clockwise):
        """Sets the clockwise of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (arc, ellipticArc) If true, the segment    is oriented clockwise from the startPoint to the endPoint around the center.  # noqa: E501

        :param clockwise: The clockwise of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: bool
        """

        self._clockwise = clockwise

    @property
    def start_point(self):
        """Gets the start_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (lineSegment, arc, ellipticArc, curvePoints=true)    The start point of the segment  # noqa: E501

        :return: The start_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point):
        """Sets the start_point of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (lineSegment, arc, ellipticArc, curvePoints=true)    The start point of the segment  # noqa: E501

        :param start_point: The start_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._start_point = start_point

    @property
    def end_param(self):
        """Gets the end_param of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (splineSegment, interpolatedSplineSegment)    The end parameter of the spline segment  # noqa: E501

        :return: The end_param of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._end_param

    @end_param.setter
    def end_param(self, end_param):
        """Sets the end_param of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (splineSegment, interpolatedSplineSegment)    The end parameter of the spline segment  # noqa: E501

        :param end_param: The end_param of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._end_param = end_param

    @property
    def start_param(self):
        """Gets the start_param of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (splineSegment, interpolatedSplineSegment)    The start parameter of the spline segment  # noqa: E501

        :return: The start_param of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._start_param

    @start_param.setter
    def start_param(self, start_param):
        """Sets the start_param of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (splineSegment, interpolatedSplineSegment)    The start parameter of the spline segment  # noqa: E501

        :param start_param: The start_param of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._start_param = start_param

    @property
    def end_point_ids(self):
        """Gets the end_point_ids of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        A 2-dimensional array of endpoint ids,    if the curve is a bounded curve.  # noqa: E501

        :return: The end_point_ids of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[str]
        """
        return self._end_point_ids

    @end_point_ids.setter
    def end_point_ids(self, end_point_ids):
        """Sets the end_point_ids of this PartStudiosGetSketchInfoResponse200GeomEntities.

        A 2-dimensional array of endpoint ids,    if the curve is a bounded curve.  # noqa: E501

        :param end_point_ids: The end_point_ids of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[str]
        """

        self._end_point_ids = end_point_ids

    @property
    def end_derivative(self):
        """Gets the end_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (interpolatedSpline[Segment]) For    a non-periodic spline the derivative at the end of the spline  # noqa: E501

        :return: The end_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._end_derivative

    @end_derivative.setter
    def end_derivative(self, end_derivative):
        """Sets the end_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (interpolatedSpline[Segment]) For    a non-periodic spline the derivative at the end of the spline  # noqa: E501

        :param end_derivative: The end_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._end_derivative = end_derivative

    @property
    def start_derivative(self):
        """Gets the start_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (interpolatedSpline[Segment]) For    a non-periodic spline the derivative at the start of the spline  # noqa: E501

        :return: The start_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._start_derivative

    @start_derivative.setter
    def start_derivative(self, start_derivative):
        """Sets the start_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (interpolatedSpline[Segment]) For    a non-periodic spline the derivative at the start of the spline  # noqa: E501

        :param start_derivative: The start_derivative of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._start_derivative = start_derivative

    @property
    def minor_radius(self):
        """Gets the minor_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (ellipse, ellipticArc) The minor radius    of the elliptic entity  # noqa: E501

        :return: The minor_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._minor_radius

    @minor_radius.setter
    def minor_radius(self, minor_radius):
        """Sets the minor_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (ellipse, ellipticArc) The minor radius    of the elliptic entity  # noqa: E501

        :param minor_radius: The minor_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._minor_radius = minor_radius

    @property
    def rational(self):
        """Gets the rational of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (spline[Segment]) If true, the spline is    in rational form  # noqa: E501

        :return: The rational of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: bool
        """
        return self._rational

    @rational.setter
    def rational(self, rational):
        """Sets the rational of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (spline[Segment]) If true, the spline is    in rational form  # noqa: E501

        :param rational: The rational of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: bool
        """

        self._rational = rational

    @property
    def curve_length(self):
        """Gets the curve_length of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (curvePoints=true) The length of the curve  # noqa: E501

        :return: The curve_length of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._curve_length

    @curve_length.setter
    def curve_length(self, curve_length):
        """Sets the curve_length of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (curvePoints=true) The length of the curve  # noqa: E501

        :param curve_length: The curve_length of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._curve_length = curve_length

    @property
    def control_points(self):
        """Gets the control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (spline[Segment]) The spline control    points  # noqa: E501

        :return: The control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[object]
        """
        return self._control_points

    @control_points.setter
    def control_points(self, control_points):
        """Sets the control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (spline[Segment]) The spline control    points  # noqa: E501

        :param control_points: The control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[object]
        """

        self._control_points = control_points

    @property
    def direction(self):
        """Gets the direction of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (line, ellipse, ellipticArc)    For line, this is the line direction. For elliptic entities, this is the direction of the major axis.  # noqa: E501

        :return: The direction of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (line, ellipse, ellipticArc)    For line, this is the line direction. For elliptic entities, this is the direction of the major axis.  # noqa: E501

        :param direction: The direction of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._direction = direction

    @property
    def degree(self):
        """Gets the degree of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (spline[Segment]) The degree of the spline  # noqa: E501

        :return: The degree of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._degree

    @degree.setter
    def degree(self, degree):
        """Sets the degree of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (spline[Segment]) The degree of the spline  # noqa: E501

        :param degree: The degree of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._degree = degree

    @property
    def end_handle(self):
        """Gets the end_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (interpolatedSpline[Segment])  For a    non-periodic spline, the end handle point use to determine the end derivative.  # noqa: E501

        :return: The end_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._end_handle

    @end_handle.setter
    def end_handle(self, end_handle):
        """Sets the end_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (interpolatedSpline[Segment])  For a    non-periodic spline, the end handle point use to determine the end derivative.  # noqa: E501

        :param end_handle: The end_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._end_handle = end_handle

    @property
    def quarter_point(self):
        """Gets the quarter_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (curvePoints=true) The point that is one    quarter way between the start and end of the curve  # noqa: E501

        :return: The quarter_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._quarter_point

    @quarter_point.setter
    def quarter_point(self, quarter_point):
        """Sets the quarter_point of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (curvePoints=true) The point that is one    quarter way between the start and end of the curve  # noqa: E501

        :param quarter_point: The quarter_point of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._quarter_point = quarter_point

    @property
    def interpolation_points(self):
        """Gets the interpolation_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (interpolatedSpline[Segment])    The interpolation points for the spline  # noqa: E501

        :return: The interpolation_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._interpolation_points

    @interpolation_points.setter
    def interpolation_points(self, interpolation_points):
        """Sets the interpolation_points of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (interpolatedSpline[Segment])    The interpolation points for the spline  # noqa: E501

        :param interpolation_points: The interpolation_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._interpolation_points = interpolation_points

    @property
    def major_radius(self):
        """Gets the major_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (ellipse, ellipticArc) The major radius    of the elliptic entity  # noqa: E501

        :return: The major_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._major_radius

    @major_radius.setter
    def major_radius(self, major_radius):
        """Sets the major_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (ellipse, ellipticArc) The major radius    of the elliptic entity  # noqa: E501

        :param major_radius: The major_radius of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._major_radius = major_radius

    @property
    def end_vector(self):
        """Gets the end_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (curvePoints=true) The tangent vector    at the end of the curve  # noqa: E501

        :return: The end_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._end_vector

    @end_vector.setter
    def end_vector(self, end_vector):
        """Sets the end_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (curvePoints=true) The tangent vector    at the end of the curve  # noqa: E501

        :param end_vector: The end_vector of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._end_vector = end_vector

    @property
    def center(self):
        """Gets the center of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (circle, arc, ellipse, ellipticArc) The center    point  # noqa: E501

        :return: The center of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (circle, arc, ellipse, ellipticArc) The center    point  # noqa: E501

        :param center: The center of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._center = center

    @property
    def number_control_points(self):
        """Gets the number_control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (spline[Segment]) The number of    control points in the spline  # noqa: E501

        :return: The number_control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: float
        """
        return self._number_control_points

    @number_control_points.setter
    def number_control_points(self, number_control_points):
        """Sets the number_control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (spline[Segment]) The number of    control points in the spline  # noqa: E501

        :param number_control_points: The number_control_points of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: float
        """

        self._number_control_points = number_control_points

    @property
    def start_handle(self):
        """Gets the start_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (interpolatedSpline[Segment]) For a    non-periodic spline, the start handle point use to determine the start derivative.  # noqa: E501

        :return: The start_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: list[float]
        """
        return self._start_handle

    @start_handle.setter
    def start_handle(self, start_handle):
        """Sets the start_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (interpolatedSpline[Segment]) For a    non-periodic spline, the start handle point use to determine the start derivative.  # noqa: E501

        :param start_handle: The start_handle of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: list[float]
        """

        self._start_handle = start_handle

    @property
    def periodic(self):
        """Gets the periodic of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        (spline[Segment], interpolatedSpline[Segment])    If true, the spline entity is periodic  # noqa: E501

        :return: The periodic of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: bool
        """
        return self._periodic

    @periodic.setter
    def periodic(self, periodic):
        """Sets the periodic of this PartStudiosGetSketchInfoResponse200GeomEntities.

        (spline[Segment], interpolatedSpline[Segment])    If true, the spline entity is periodic  # noqa: E501

        :param periodic: The periodic of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: bool
        """

        self._periodic = periodic

    @property
    def is_construction(self):
        """Gets the is_construction of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501

        Set to true if this is a construction    entity  # noqa: E501

        :return: The is_construction of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :rtype: bool
        """
        return self._is_construction

    @is_construction.setter
    def is_construction(self, is_construction):
        """Sets the is_construction of this PartStudiosGetSketchInfoResponse200GeomEntities.

        Set to true if this is a construction    entity  # noqa: E501

        :param is_construction: The is_construction of this PartStudiosGetSketchInfoResponse200GeomEntities.  # noqa: E501
        :type: bool
        """

        self._is_construction = is_construction

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PartStudiosGetSketchInfoResponse200GeomEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
