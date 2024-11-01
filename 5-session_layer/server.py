import grpc
from concurrent import futures
import session_pb2
import session_pb2_grpc


class SessionManager(session_pb2_grpc.SessionManagerServicer):
    def start_session(self, request, context):
        return session_pb2.SessionResponse(message = f"Session {request.session_id} starts.")
    
    def end_session(self, request, context):
        return session_pb2.SessionResponse(essage = f"Session {request.session_id} ends.")
    
def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    session_pb2_grpc.add_SessionManagerServicer_to_server(SessionManager(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server starts on port 50051...")
    server.wait_for_termination()

serv()