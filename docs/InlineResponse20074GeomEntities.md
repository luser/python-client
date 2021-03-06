# InlineResponse20074GeomEntities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity. Can be one of:    \&quot;point\&quot;, \&quot;line\&quot;, \&quot;lineSegment\&quot;, \&quot;circle\&quot;, \&quot;arc\&quot;, \&quot;ellipse\&quot;, \&quot;ellipticArc\&quot;, \&quot;spline\&quot;, \&quot;splineSegment\&quot;,    \&quot;interpolatedSpline\&quot;, \&quot;interpolatedSplineSegment\&quot;, \&quot;unknownGeometry\&quot;. | [optional] 
**end_point_ids** | **list[str]** | A 2-dimensional array of endpoint ids,    if the curve is a bounded curve. | [optional] 
**point** | **list[float]** | (line) An arbitrary point on the line | [optional] 
**direction** | **list[float]** | (line, ellipse, ellipticArc)    For line, this is the line direction. For elliptic entities, this is the direction of the major axis. | [optional] 
**start_point** | **list[float]** | (lineSegment, arc, ellipticArc, curvePoints&#x3D;true)    The start point of the segment | [optional] 
**end_point** | **list[float]** | (lineSegment, arc, ellipticArc, curvePoints&#x3D;true) The end point of the segment | [optional] 
**center** | **list[float]** | (circle, arc, ellipse, ellipticArc) The center    point | [optional] 
**radius** | **float** | (circle, arc). The circular radius | [optional] 
**major_radius** | **float** | (ellipse, ellipticArc) The major radius    of the elliptic entity | [optional] 
**minor_radius** | **float** | (ellipse, ellipticArc) The minor radius    of the elliptic entity | [optional] 
**clockwise** | **bool** | (arc, ellipticArc) If true, the segment    is oriented clockwise from the startPoint to the endPoint around the center. | [optional] 
**periodic** | **bool** | (spline[Segment], interpolatedSpline[Segment])    If true, the spline entity is periodic | [optional] 
**rational** | **bool** | (spline[Segment]) If true, the spline is    in rational form | [optional] 
**degree** | **float** | (spline[Segment]) The degree of the spline | [optional] 
**number_control_points** | **float** | (spline[Segment]) The number of    control points in the spline | [optional] 
**control_points** | **list[object]** | (spline[Segment]) The spline control    points | [optional] 
**knots** | **list[float]** | (spline[Segment]) The spline knot vector | [optional] 
**start_param** | **float** | (splineSegment, interpolatedSplineSegment)    The start parameter of the spline segment | [optional] 
**end_param** | **float** | (splineSegment, interpolatedSplineSegment)    The end parameter of the spline segment | [optional] 
**start_handle** | **list[float]** | (interpolatedSpline[Segment]) For a    non-periodic spline, the start handle point use to determine the start derivative. | [optional] 
**end_handle** | **list[float]** | (interpolatedSpline[Segment])  For a    non-periodic spline, the end handle point use to determine the end derivative. | [optional] 
**start_derivative** | **list[float]** | (interpolatedSpline[Segment]) For    a non-periodic spline the derivative at the start of the spline | [optional] 
**end_derivative** | **list[float]** | (interpolatedSpline[Segment]) For    a non-periodic spline the derivative at the end of the spline | [optional] 
**interpolation_points** | **list[float]** | (interpolatedSpline[Segment])    The interpolation points for the spline | [optional] 
**is_construction** | **bool** | Set to true if this is a construction    entity | [optional] 
**curve_length** | **float** | (curvePoints&#x3D;true) The length of the curve | [optional] 
**mid_point** | **list[float]** | (curvePoints&#x3D;true) The point that is half    way between the start and end of the curve | [optional] 
**quarter_point** | **list[float]** | (curvePoints&#x3D;true) The point that is one    quarter way between the start and end of the curve | [optional] 
**start_vector** | **list[float]** | (curvePoints&#x3D;true) The tangent vector    at the start of the curve | [optional] 
**end_vector** | **list[float]** | (curvePoints&#x3D;true) The tangent vector    at the end of the curve | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


